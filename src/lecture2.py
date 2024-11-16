import numpy as np
import pandas as pd
import json

######################################################################################################
##  DATA CLEANING AND PREPARATION                                                                   ##
######################################################################################################

# https://archive.ics.uci.edu/dataset/10/automobile
file_name = "../assets/imports-85.data"
# Read the data
df = pd.read_csv(file_name, header=None)
# If the file has headers, use the following
# df = pd.read_csv(file_name, header=0)
print(df.head())
print("#" * 50)
# To see what the data set looks like, we'll use the head() method.
pd.set_option('display.max_columns', None)
print(df.head())
print("#" * 50)
print(df.info())
print("#" * 50)
# list the data types for each column
print(df.dtypes)
print("-" * 50)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers
print(df.head())
print("#" * 50)
print(df.info())
print("#" * 50)
# list the data types for each column
print(df.dtypes)
print("-" * 50)

######################################################################################################
##  Step 1: CONVERT DATA TYPE FROM OBJECT TO NUMERIC                                                ##
######################################################################################################
# Replace "?" with NaN
df.replace("?", np.nan, inplace=True)

# Inspect float and int columns
print(df.describe())
# From looking into head() and info() methods, we can see that the following columns are float or int:
# Float: wheel-base  length  width  height    bore  stroke  compression-ratio  horsepower
# Int: symboling  normalized-losses curb-weight  engine-size peak-rpm  city-mpg  highway-mpg  price

#  OK 0   symboling          205 non-null    int64
#  ==>1   normalized-losses  205 non-null    object
#  2   make               205 non-null    object
#  3   fuel-type          205 non-null    object
#  4   aspiration         205 non-null    object
#  5   num-of-doors       205 non-null    object
#  6   body-style         205 non-null    object
#  7   drive-wheels       205 non-null    object
#  8   engine-location    205 non-null    object
#  OK9   wheel-base         205 non-null    float64
#  OK10  length             205 non-null    float64
#  OK11  width              205 non-null    float64
#  OK12  height             205 non-null    float64
#  OK13  curb-weight        205 non-null    int64
#  14  engine-type        205 non-null    object
#  15  num-of-cylinders   205 non-null    object
#  OK16  engine-size        205 non-null    int64
#  17  fuel-system        205 non-null    object
#  ==>18  bore               205 non-null    object
#  ==>19  stroke             205 non-null    object
#  20  compression-ratio  205 non-null    float64
#  ==>21  horsepower         205 non-null    object
#  ==>22  peak-rpm           205 non-null    object
#  OK23  city-mpg           205 non-null    int64
#  OK24  highway-mpg        205 non-null    int64
#  ==>25  price              205 non-null    object

# Convert the data types to float
toFloatColumns = ["normalized-losses", "bore", "stroke", "horsepower", "peak-rpm", "price"]
for column in toFloatColumns:
    # This line attempts to cast all values in the specified column to floats.
    # If the column contains any non-numeric values, this operation will raise an error.
    # So don't use it
    # df[column] = df[column].astype("float")
    df[column] = pd.to_numeric(df[column], errors='coerce')

#     Convert the data types to int
toIntColumns = ["normalized-losses", "peak-rpm", "price"]
for column in toIntColumns:
    df[column] = df[column].astype('Int64')


######################################################################################################
##  Step 2: Identify and handle missing values                                                      ##
######################################################################################################

# Showing the method Value_counts() to see the number of unique values in a column
# value_counts() method
print("========================" * 50)
print(df['num-of-doors'].value_counts(dropna=False))
print("-" * 50)
# Identify columns with missing values
missing_values = df.isnull()
print(missing_values.head())

for column in missing_values.columns.values.tolist():
    true_counts = missing_values[column].value_counts()
    print(f"{column}: {true_counts}")
print("-" * 50)
for column in missing_values.columns.values.tolist():
    true_counts = missing_values[column].value_counts().get(True, 0)  #0 if not present
    if (true_counts > 0):
        print(f"{column}: {true_counts}")

# normalized-losses: 41
# num-of-doors: 2
# bore: 4
# stroke: 4
# horsepower: 2
# peak-rpm: 2
# price: 4
print("-" * 50)

# Replace missing values with the mean
replaceWithMeanColumns = ["normalized-losses", "bore", "stroke", "horsepower", "peak-rpm"]
for column in replaceWithMeanColumns:
    print("Processing {} column".format(column))
    avg = df[column].mean()
    if(df.dtypes[column] == "float64"):
        avg = round(avg, 2)
    else:
        avg = round(avg)
    print("Average of " + column + ": " + str(avg))

    # df[column].replace(np.nan, avg, inplace =True) # Will be deprecated
    df[column] = df[column].replace(np.nan, avg)

# Replace with the most common value
print(df['num-of-doors'].value_counts(dropna=False))
commonType = df['num-of-doors'].value_counts().idxmax()
print("common type of cars is " + commonType)
df["num-of-doors"] = df["num-of-doors"].replace(np.nan, commonType)
print(df['num-of-doors'].value_counts(dropna=False))
print("-" * 50)

# Drop the rows with missing values in the price column
df = df.dropna(subset=["price"], axis=0)

# Reset the index
df.reset_index(drop=True, inplace=True)

######################################################################################################
##  Step 3: CONVERT TO STANDARD UNITS                                                               ##
######################################################################################################
toCm = ["length", "width", "height"]
# 1 inch = 2.54 cm
for column in toCm:
    df[column] = df[column] * 2.54
    # columnMin = df[column].min()
    # columnMax = df[column].max()
    # df[column] = (df[column] - columnMin) / (columnMax - columnMin)

######################################################################################################
##  Step 4: NORMALIZATION                                                                           ##
######################################################################################################
# Min - Max Normalization
#  This method shifts the values of each feature so that the minimum value of each feature will be 0,
#  and the maximum value of each feature will be 1.
# This is done so that the effect of each variable in the model is proportional to the other variables.

columList = df.columns.tolist()
for column in columList:
    print("Processing {} column of {} type".format(column, df[column].dtype))
    if df[column].dtype != "object":
        columnMin = df[column].min()
        columnMax = df[column].max()
        df[column] = df[column].astype('float64')
        df[column] = round((df[column] - columnMin) / (columnMax - columnMin), 3)



######################################################################################################
##  Step 4: HANDLING STRINGS                                                                        ##
######################################################################################################
columList = df.columns.tolist()
for column in columList:
    if df[column].dtype == "object":
        print("\nProcessing {} column of {} type".format(column, df[column].dtype))
        df[column] = df[column].str.lower()
        print(df[column].value_counts())

# This list of list is used to store the columns that are one-hot encoded
one_shot_columns = []
for column in columList:
    if df[column].dtype == "object":
        print("\nProcessing {} column of {} type".format(column, df[column].dtype))
        df[column] = df[column].str.upper()
        #default dtype is boolean, prefix to chane gas --> fuel-gas
        dummy_variable = pd.get_dummies(df[column], prefix=column, dtype=int)
        for dummy in dummy_variable.columns.tolist():
            dummy_variable.columns = dummy_variable.columns.str.lower()
        one_shot_columns.append(dummy_variable.columns.tolist())
        df = pd.concat([df, dummy_variable], axis=1)
        df = df.drop(column, axis = 1)

######################################################################################################
##  Step 5: SAVING PROCESSED CVS                                                                    ##
######################################################################################################
df.to_csv("../assets/cars-processed.csv", index=False)
print(one_shot_columns)
with open('../assets/one_shot_columns.json', 'w') as file:
    json.dump(one_shot_columns, file)
