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
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)


def recursion(number):
    if (number > 0):
        result = number+recursion(number-1)
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
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


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
