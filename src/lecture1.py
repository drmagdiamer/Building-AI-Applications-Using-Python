x = 5
print(x)
# 5
print(type(x))
# <class 'int'>
x = "Hello, World!"
print(x)
# Hello, World!
print(type(x))
# <class 'str'>
x = 3.14
print(x)
# 3.14
print(type(x))
# <class 'float'>

x = 3 == 5
print(x)
# False
print(type(x))
# <class 'bool'>
print("-------------------")
valueStr = input('Enter a number: ')
a = int(valueStr)

# In Java
# if (a == 5) {
#     print('The variable a is 5');
#     }

if a == 5:
    print('The variable a is 5')
    print("In Python, no { } and no ;")
else:
    print('The variable a is not 5')

print("-------------------")
print(17 / 5)
print(17.0 / 5)
# 3.4
# 3.4
print(17 // 5)
print(17.0 // 5)
# 3
# 3.0
print(17 % 5)
print(17.0 % 5)
# 2
# 2.0
print("-------------------")
print(type('This is a string. O\'Relly. I said: "Hello"'))
print(type("And so is this. O'Relly. I said: \"Hello\""))
print(type("""and this."""))
print(type('''and even this...'''))  # triple quoted strings can span multiple lines
print('''
O'Relly. 
I said: "Hello"
and even this...
and I continue here.
and here
''')

print("-------------------")
x = 6  # initialize x
print(x)  # 6
x += 3  # increment x by 3; same as x = x + 3
print(x)  # 9
x -= 1  # decrement x by 1
print(x)  # 8
x *= 2  # multiply x by 2
print(x)  # 16
x /= 4  # divide x by 4
print(x)  # 4.0
x **= 2  # x to the power of 2
print(x)  # 16.0
x %= 5  # remainder of x divided by 5
print(x)  # 1.0
print("-------------------")
print(3.14, int(3.14)) #3.14 3
print(3.9999, int(3.9999))  #3.9999 3
# This doesn't round to the closest int!
print("2345", int("2345"))  #2345 2345
# parse a string to produce an int
print(float("123.45")) # 123.45
age  = 25
name = "Mike"
# print("Hi" + name + " your age is " + age + " years old.")
print("Hi" + name + " your age is " + str(age) + " years old.")

print("-------------------")

total = 0
for x in range(5):
    total += x
    print(f"Adding X {x}, sum so far is {total}")
# Adding X 0, sum so far is 0
# Adding X 1, sum so far is 1
# Adding X 2, sum so far is 3
# Adding X 3, sum so far is 6
# Adding X 4, sum so far is 10
for y in range(4, 6):
    total += y
    print(f"Adding Y {y}, sum so far is {total}")
# Adding Y 4, sum so far is 14
# Adding Y 5, sum so far is 19
print("-------------------")

l = ['a', 'b', 'c', 'd', 'a'] # list. Duplicate values are allowed.

t = ('a', 'b', 'c', 'd', 'b') # tuple (immutable list). Duplicate values are allowed.

print(l)
# ['a', 'b', 'c', 'd', 'a']
print(t)
# ('a', 'b', 'c', 'd', 'b')

print(f'type of l is  {type(l)}')
print(f'type of t is  {type(t)}')
# type of l is  <class 'list'>
# type of t is  <class 'tuple'>
l[1] = 'changed'
print(l)
# ['a', 'changed', 'c', 'd', 'a']
for s in l:
    print(s)
# a
# changed
# c
# d
# a
print("-------------------")
data = [1,2, 8 ,12]
print(data[0])
# 1
print(data[1])
# 2
print(data[2])
# 8
print(data[-1])
# 12
print(data[-2])
# 8

print("-------------------")
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name, score = person
    print("Hello " + name + ". Your score is " + str(score))

print("-------------------")
fruit = ["banana", "apple", "cherry"]
print(fruit)
fruit[0] = "pear"
fruit[-1] = "orange"  #last element of a list
print(fruit)
#['pear', 'apple', 'orange']
print("-----------")
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']  # from item =1 (2nd) to item = 3 (4th) [NOT INCLUDED] replace with x and y
print(alist)
#['a', 'x', 'y', 'd', 'e', 'f']
print("-------------------")
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)
# [5, 27, 3, 12]
total = 0
for i in mylist:
    total += i
print(total)
print("-------------------")
print("#################################")
c = ["apple", "orange"]
d = ["apple", "orange"]
print(c is d)
# False
print(c == d)
# True
print(id(c))
print(id(d))
x = c
print(c is x)
# True
print(id(c))
print(c == x)
# True
c.append("banana")
print(c == d)
# False
print(c == x)
# True
print(x)
# ['apple', 'orange', 'banana']

print("-------------------")
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)
# {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print("-----------------")
eng2sp_2 = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp_2)
# {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print("-----------------")
value = eng2sp['two']
print(value)
# dos
print("-----------------")
total = 0
mydict = {'cat': 12, 'dog': 6, 'elephant': 23, 'bear': 20}
for key in mydict:
    if len(key) == 3:
        total += mydict[key]
print(total)
# 18
print("-----------------")
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))
    #OR
    print("Hello {}. Your score is {}.".format(name, score))
    # Hello Rodney Dangerfield. Your score is -1
    # Hello Marlon Brando. Your score is 1
    # Hello You. Your score is 100

print("-----------------")
origPrice = float(input('Enter the original price: $'))  #5
discount = float(input('Enter discount percentage: '))  #10
newPrice = (1 - discount / 100) * origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)
first_name = "Peter"
last_name = "Huang"
score = 96.75
print(f"Hello {first_name + ' ' + last_name}. Your score is {90 + 6.75:.3f}.")
# Hello Peter Huang. Your score is 96.750.
print(f"Hello {first_name} {last_name}. Your score is {score:.3f}.")
# Hello Peter Huang. Your score is 96.750. [THE SAME]
print(f'Hello {first_name} {last_name}. Your score is {score:.3f}.')
# Hello Peter Huang. Your score is 96.750. [THE SAME]
print("-----------------")


def square(x):
    return x * x


def sub(x, y):
    return x - y


print(square(3))
square(5)
print(sub(6, 4))
print(sub(5, 9))
print("-----------------")


def f(x, y=3, z=5):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

f(2)
# x, y, z, are: 2, 3, 5
f(2, z=7)
# x, y, z, are: 2, 3, 7
f(2, 5)
# x, y, z, are: 2, 5, 5
print("-----------------")


def cheeseshop(kind, list, dictionary):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in list:
        print(arg)
    print("-" * 40)
    for kw in dictionary:
        print(kw, ":", dictionary[kw])


aList = ["It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            "It's a bit runny, sir.",
            "It's not runny at all, sir."]
aDict = {"shopkeeper": "Michael Palin",
            "client": "John Cleese",
            "sketch": "Cheese Shop Sketch"}
cheeseshop("Limburger", aList, aDict)


def cheeseshop2(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
print("#" * 40)
cheeseshop2("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print("-----------------")

def f(x):
    return x - 1


print(f)
# <function f at 0x7f8b1f7b7d08>
print(type(f))
# <class 'function'>
print(f(3))
# 2

print(lambda x: x - 2)
# <function <lambda> at 0x7f8b1f7b7d90>
print(type(lambda x: x - 2))
# <class 'function'>
print((lambda x: x - 2)(6))
# 4
print("--------------------")
# create a function that takes a string and returns the last character in that string
# using a lambda function
last_char = (lambda s: s[-1])
print(last_char("hello"))
print("--------------------")


def output(student, PS1, PS2):
    return "{} got {} in PS1 and {} in PS2.".format(
        student, PS1, PS2)


# Equivalent lambda function
output2 = lambda s, p1, p2: "{} got {} in PS1 and {} in PS2.".format(s, p1, p2)

print(output2("Mike", 60, 70))

print("--------------------")
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return "Age is valid"

try:
    print(check_age(16))
except ValueError as e:
    print(e)
