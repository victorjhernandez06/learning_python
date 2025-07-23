"""Python Polymorphism"""
# The word "Polymorphism" means "many forms", and in programming it refers ti methods/functions/operators with the same name that can be executed on many objects or class.

"""Function Polymorphism"""
# An example of a python function that can be used on different objects is the len() function.

"""String"""
# For strings len() returns the number of characters.
# Example:
x = "Hello World!"
print(len(x)) #--> 12

"""Tuple"""
# For tuple len() returns the number of items in the tuple:
mytuple = ('Computer','Laptop','Tablet')
print(len(mytuple)) #--> 3

"""Dictionary"""
# For dictionaries len() returns the numbers of key/value pairs in the dictionary.
thisdict = {
    'brand' : 'Dell',
    'model' : 'Alienware',
    'Year': 2024
}
print(len(thisdict)) # --> 3

"""class Polymorphism"""
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name
# for example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
# Example: Different classes with the same method:
class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand =  brand
        self.model =  model

    def move(self):
        print("Fly!")

car1 = Car('ford','Mustang')
boat1 = Boat('Ibiza','Tour 2025')
plane1 = Plane('Boeing','747')

for x in (car1, boat1, plane1):
    x.move()
