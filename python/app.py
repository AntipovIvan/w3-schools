import random

print("Hello, World!")

if 5 > 2:
    print("Five is greater that two!")

x = 5
y = "Hello Worldee!"
z = float(3.5)
print(x)
print(y)
print(type(z))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

glob = "awesome"


def myfunc():
    glob = "fantastic"
    print("Python is " + glob)


myfunc()
print("Python is " + glob)


print(random.randrange(1, 10))


multiline = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline)


word = "Ivan"
for dash in word:
    print(dash)
print(word[1:3])


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))


def myFunc():
    print("This is a func")


myFunc()


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)


def recursion(number):
    if number > 0:
        result = number + recursion(number - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
recursion(3)


def lambdaFunc(n):
    return lambda a: a * n


mydoubler = lambdaFunc(2)
mytripler = lambdaFunc(3)

print(mydoubler(11))
print(mytripler(11))


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)


person = Person("Ivan", 32)

print(person)
person.myfunc()


class Human:
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


human = Human("Ivan", "Antipov")
human.printname()


class Student(Human):
    def __init__(self, fname, lname, year) -> None:
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear,
        )


person2 = Student("Irina", "Ivanovna", 2015)
person2.printname()
person2.welcome()


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


# Polymorphism
class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("Move! " + self.brand + self.model)


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail! " + self.brand + self.model)


class Plane(Vehicle):
    def move(self):
        print("Fly! " + self.brand + self.model)


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Sukhoi", "Superjet")

for x in (car1, boat1, plane1):
    x.move()

import mymodule as mx

mx.greeting("Ivan")
moduleperson = mx.person1["age"]
print(moduleperson)


import platform

system = platform.system()
print(system)
allFuncs = dir(platform)
print(allFuncs)

from mymodule import person1

print(person1["age"])


import datetime

time = datetime.datetime.now()
print(time.year)
print(time.strftime("%A"))
print(time.strftime("%B"))


import json

js = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1},
    ],
}

print(json.dumps(js))
print(json.dumps(js, indent=4))


# some JSON:
jsdata = '{ "name":"John", "age":30, "city":"New York"}'

# parse
parseJsdata = json.loads(jsdata)

# the result is a Python dictionary:
print(parseJsdata["age"])


import re

txt = "The rain in Spain"
isTxt = re.search("^The.*Spain$", txt)

if isTxt:
    print("YES! We have a match!")
else:
    print("No match")


try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


# username = input("Enter username:")
# print("Username is: " + username)


myorder = "I have a {carname}, it is a {model}.\n"
print(myorder.format(carname="Ford", model="Mustang"))

file = open("demofile.txt", "r")
# print(file.read())
# print(file.readline())

for x in file:
    print(x)

file.close()


file2 = open("demofile.txt", "a")
file2.write("\nNow the file has more content!")
file2.close()

# open and read the file after the appending:
file2 = open("demofile.txt", "r")
print(file2.read())
file2.close()

file3 = open("myfile.txt", "x")
file3.close()

# import os

# if os.path.exists("myfile.txt"):
#     os.remove("myfile.txt")
# else:
#     print("The file does not exist")


def backwards(string):
    return string[::-1]


print(backwards("Random String!"))


removeDupes = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(removeDupes))
print(mylist)
