import math

print(dir(math))  #shows all the functions in the module


def average(*numbers):  # *number will give Tuple
    sum = 0
    for i in numbers:
        print(i)
        sum = sum + i
    print("The Average is:", round(sum / len(numbers)))


average(5, 1000000, 5666)


def Dict(**KVP):  # **KVP is a Dictionary
    print("Personal Details")
    print("Name:", KVP["N"])
    print("Sports:", KVP["S"])
    print("Age:", KVP["A"])


N = input("Enter Name:")
S = input("Favourite Sport:")
A = int(input("Your Age:"))
Dict(N=N, S=S, A=A)

M = [2, 3, 4, 5, "Archisman", "Football", True]
print(M[-3])
print(M[len(M) - 3])

list = []
for i in range(2, 10, 2):
    list.append(i)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.insert(3, 77)
print(list)

#To put a list into another list
L = [2, 3, 4, 5, 6, 7, 8]
M = [900, 98866, 7566]
L.extend(M)
print(L)

name = 'Archisman'
country = 'India'
print(f"Hey my name is {name} and I am from country {country}")
price = 49.4560033
text = f"For only {price:0.2f} dollar"
print(text)


def remainder(a, b):
    '''Takes two no. , divides it and returns remainder'''  #Docstring
    if a >= b:
        print("The remainder is:", a % b)
    else:
        print("The remainder is:", b % a)


remainder(12, 5)
print(remainder.__doc__)

#The Zen of Python
import this


#_______________________
#FibonacciSequence
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for t in range(int(input("enter number : "))):
    print(fib(t))

#Methods in SETS
S1 = {1, 4, 6, 8, 34, 55, 23, 67}
S2 = {2, 3, 5, 7, 88, 35, 23, 67}
#1. Union of sets
S = S1.union(S2)
print(S)
print(S1, S2)
S1.update(S2)
print(S1)
#2. Intersection of sets
S5 = {1, 4, 6, 8, 34, 55, 23, 67}
S6 = {2, 3, 5, 7, 88, 35, 23, 67}
S4 = S5.intersection(S6)
print(S4)

cities3 = {"Delhi", "Mumbai", "Kolkata", "Hyderabad"}  #Case sensitive
cities4 = {"delhi", "Kolkata", "Bangalore", "Ladakh"}  # Delhi Not Equal to delhi
cities3.intersection_update(cities4)
print(cities3)

#Symmetric difference : Jo common nahi hai unko display nahi karega
T = {1, 3, 5, 7, 9, 11, 13, 15, 17, 219}
Y = {2, 3, 5, 7, 11, 13, 17, 19}
Y.add("Helsinki")
X = T.symmetric_difference(Y)
print(X)
if "Helsinki" in Y:
    print("Yes")
else:
    print("No")

dict = {"name": "karan", "age": 19, "eligible": True}
print(dict)
print(dict["eligible"])
print(dict.get("eligible"))
print(dict.keys())
print(dict.values())
for i in dict.keys():
    print(i)

for key, value in dict.items():
    print(f"The value corresponding to the key {key} is {value}")

#For and Else together
for i in range(0, 5):
    print(i)
else:
    print("Sorry NO i")

p = 0
while p < 7:
    print(p)
    p = p + 1
else:
    print("P not found")

a = input("Enter a Number:")
print(f"Multiplication Table of {a}:")
try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a) * i}")
except:
    print("Error!!")
finally:  # whether ur code generates result or error finally: will always be executed. So any waork like close file or break it will work
    print("I am always executed")


def func():
    try:
        l = [1, 2, 4, 5, 7, 8]
        i = int(input("Enter the index:"))
        print("The no. is:", l[i])
        return 1
    except:
        print("Some error occur")
        return 0
    finally:
        print("I'm always executed")


x = func()
print(x)

a = int(input("Enter no. b/w 5 to 9:"))
if (a < 5 or a > 9):
    raise ValueError("Value should be b.w 5 and 9")
    # Exceptions : AttributeError, EOFError, ImportError,
    #ModuleNotFoundError, IndexError.
else:
    pass

F = input("Enter:")
if F == "Quit":
    print("OK")
else:
    raise NameError("Enter Quit")

a = 333000
b = 3300
c = 9 if a > b else 0
print(c)
d = 10 if b > a else 2
print(d)

a = [123, 234, 345, 456, 567, 678, 789, 890, 901, 102]
for index, i in enumerate(a, start=1):  #start=1 will make index from 1 and not from 0
    print(index, i)

import os

folders = os.listdir("data")
#for files in folders:
#print(files)
for folder in folders:
    print(os.listdir(f"data/{folder}"))

x = 10


def func():
    global x  # will change global x = 10 to 4
    x = 4
    y = 7
    print(y)


func()
print(x)

#writing a function
avg = lambda x, y, z: print("Avg: ", (x + y + z) / 3)
avg(5, 6, 7)


def app(fx, value):
    return 6 + fx(value)


cube = lambda x: x ** 3
print(cube, 2)

#Map or Mapping
square = lambda x: x ** 2
l = [1, 2, 3, 4, 5, 6]
newl = map(square, l)
print(tuple(newl))


#Filter
def filter_items(a):
    return a > 4


#Function ko jo function as a argument le le
# wo Higher order function kehte hai, ex: MAP and Filter
newnewl = tuple(filter(filter_items, l))
print(newnewl)

from functools import reduce

N = [1, 2, 3, 4, 5]


def sum(x, y):
    return x + y


JJ = reduce(sum, N)
print(JJ)

# "is" exact location of a object in memory
# "==" as compared to the object
#values which are immutable returns true in every case
a = 4  #int is immutable
b = "4"
print(a is b)
print(a == b)

#To check a year is leap year or NOT
import calendar as cal

print(cal.isleap(2024))


#About OOPS concept
#Object Oriented Programming
#Railway_Form ---> Class [Blueprint]
#Harry ---> harry ki infor form --->object [entity]
#Tom ---> Tom ki infor form --->object [entity]
#Jack ---> Jack ki infor form --->object [entity]

class Person:  #class is a general form
    name = "Archisman"
    occupation = "AI Engineer"
    networth = 1000

    def info(self):
        print(f"{self.name} is {self.occupation}")
        #self  ka matlab wo object jiske liye koi method call kia ja raha hai i.e
        #[self parameter is an reference to the current instance of the class and
        # is used to access variables that belong to the class]


d = Person()  #d becomes a object
d.info()

a = Person()
a.name = "Jatin"
a.occupation = "Software developer"

b = Person()
b.name = "Nitika"
b.occupation = "HR"

a.info()
b.info()


#Constructors : A special method to create and initialize an object of a class
class People:
    def __init__(self, n, o):  #__init__() is a constructor
        print("Hello!")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = People("Archisman", "Automobile Engineer")
b = People("Divya", "HR")
a.info()
b.info()


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This"+self.model+"car is driving")

    def stop(self):
        print("This"+self.model+"car is stopped")


car_1 = Car("Chevy", "Corvette", 2021, "Blue")
print(car_1.make)
car_1.drive()


# *args : arguments are taken as Tuple
def add(*args):  # *args can be renamed. Ex: *stuff
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))


# **kwargs : arguments taken as dictionary
def hello(**kwargs):
    print("Hello" + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Bro", middle="Dude", last="Code")


# Decorators
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!!")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx()


# *args : arguments are taken as Tuple
# **kwargs : arguments taken as dictionary
@greet  #Decorator
def hello():
    print("Hello World!!")


# Decorators help in applying a specific task again and again
@greet
def add(a, b):
    print(a + b)


hello()  # We don't need to call decorator while calling a function
add(1, 3)


class MyClass:
    @property
    def ten_value(self):
        return self._ten_value

    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_values(self):
        return 10* self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

# same function which is  made  to
# behave as a setter as well as a
# getter  ,when we use "property "
# attribute it behaves like a getter
# and when we use "setter" attribute
# is behaves like a setter

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

# Inheritance in Python
# WHen a class derives from another class
class Employee: # Pappa Class
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDet(self):
        print(f"The name of Employee:{self.id} is {self.name}")

class Programmer(Employee): # Son CLass
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("Rohan Das", 400)
e1.showDet()
e2 = Programmer("Harry", 410)
e2.showLanguage()

''' Static Method belongs to a class rather than an 
instance of class. @staticmethod'''
class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a+b

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)



