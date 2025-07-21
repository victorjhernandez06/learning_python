"""Python Classes and Objects"""
# Almmost everthingn in Python is an object. with its properties and Methods.
# A class is like an object constructor, or a "Blueprint" for creating objects.

"""Create a Class"""
# to create a class, use a the keyword class:
# Example: Create a class named MyClass, with a property named x:

class MyClass:
    x = 5
    
"""Create a Object"""
# How we can use the class named MyClass to create objects:
# Example: Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x) # --> 5

"""The __init___() Function"""

# The examples aboves are classes and objects in their form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(). which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.

# Example: Create a class named Person, use the __init__() function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Victor', 42)

print(p1.name) #--> Victor
print(p1.age) #--> 42

# Note: the __init__() function is called automatically every time th ne class is being used to create a new object

"""The __str__() Fucntion"""
# the __str__() function contros what shoud be returned when the class object is represented as a string.
# Is the __str__() function is not set, the string representation of the obect is returned.

# Example
# The string representation og an object WITHOUT the __str__() function:

class People:
    def __init__(self, name, age):
        self.name =  name
        self.age = age
p1 = People('Sofia', 9)
print(p1) # --> <__main__.People object at 0x7f3fd3912950>

# the string representation of an object WITH the __str__() function.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
p1=Person('Karina', 41)
print(p1) #--> Karina (41)

"""Objects Methods"""
#The objects Methods can also contain methods, Methods in objects are functions thatbelong to teh object.
# Let us reate a method the Person class

# Example: Insert a function that prins a greeting, and execute it in the p1 object. 

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print (f"Hello, my name is: {self.name} and I am {self.age} years old.")
        print("Hello, my name is: " + self.name + " and i am " + str(self.age) + " years old.")
        
p1 = Person('Adrian', 16)
p1.myfunc() # --> Hello, my name is: Adrian and I am 16 years old.

#note: The self parameter, is a reference tto the current instance of the class, and is used to access variables that belong to the class.

""" The self parameter"""

#the Self parameter is a reference of the curren instance of the class, and is used to access variable that belong in the class.

#It does not have to be named self, can you call it whatever you like, but it has to be the first parameter of any funtion in the class.

#Example
#use the words mysillyobject and abc instead of self.

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
        
    def myfunc(abc):
        print("Hello my name is: " + abc.name)
        
p1 = Person('Victor', 43)
p1.myfunc() 

"""Modify Object Properties"""

#You can modify properties on aobjects like this:
p1.age = 40
print(p1.age)

"""Delete Object Properties"""
#you can delete properties on objects by using the del keyword
#example: Delete the age property from the p1 object:

del p1.age

"""Delete Objects"""
# You can delete objects by using the del keyword
#Example: delete the p1 object
del p1

"""the pass statement"""
# Class definitions cannot be empty, but if you some reason have a class definition with no content, put in the pass statement to avoid geting an error.

class Person: 
    pass

# Exercise
