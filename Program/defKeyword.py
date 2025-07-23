"""Python def Keyword"""

# defining function
def func():
    print("Hello")

# Calling
func()

# -> Hello

"""
Function's Structure

def function_name (parameters):
    Statement
    return expression
## def --> Keyword
## function_name  --> function name
## (parameters)  --> parameters
## statement --> Body of statement
## return  --> function return
"""

# In the case of classes, the def keyword is used for defining the methods of a class
# def keyword is also required to define the special member of a class like __init__
# La palabra clave def tambien es necesaria para definir una funcion miembro especial
# de una clase como __init()__

"""Create function to find the subtraction of two Numbers"""
# Python 3 code to demostrate
# def keyword
#function for subtraction of 2 numbers
def subNumbers(x,y):
    return(x - y)

# main code
a = 90
b = 50

# Finding subtraction
res = subNumbers(a,b)

#print statement
print("subtration of", a, "and", b, "is", res)
#-> subtration of 90 and 50 is 40

"""Create function with the first 10 prime numbers"""

#a function name print is defined
# using def

# def fun (n):
#     x =2
#     count = 0
#     while count < n:
#         for d in range(2, int(x **0.5)+ 1): #check divisibility only up to sqrt(x)
#             if x % d == 0:
#                 break #if divisible, it's not prime, so break the loop
#             else:
#                 print(x) # Prime number
#                 count +=1
#             x +=1
# # Driver code
# n = 10
# fun (n)

"""Passing Function as an Argument"""

# A function that takes another function as an argument
def fun (func, arg):
    return func(arg)

def square(x):
    return x ** 2

#Calling fun and passing square function as an argument
res = fun(square, 5)
print(res)


# A function that takes another function as an argument
def fun(func, arg):
    return func(arg)


def square(x):
    return x ** 2


# Calling fun and passing square function as an argument
res = fun(square, 5)
print(res)

"""Python def keyword example with *args"""
# *args is used ti pass a variable number of arguments to a function.

def fun(*args):
    for arg in args:
        print(arg)
#calling the function witb multiple arguments
fun(1, 2, 3, 4, 5)
# 1
# 2
# 3
# 4
# 5

"""Python def keyword example with **kwargs"""
# *kwargs is used to pass variable number of keyword arguments to a function.
# *kwargs es utilizada para pasar una cantidad variable de argumentos de palabras clave en una funcion.

def fun(**kwargs):
    for k, val in  kwargs.items():
        print(f'{k}: {val}')
# calling the function with keyword arguments
fun (name ='alice', age=30, city = 'New York')

#name: alice
# age: 30
# city: New York


"""Python def keyword example with the class"""
class Person:
    # construir to initialize the person's name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Methods to print a greeting message
    def greet(self):
        print(f'Name - {self.name} and Age - {self.age}.')

# Create a instance of the Person Class
p1 =  Person("Alice", 30)

# Call the great method to display the greeting message
p1.greet()

# -> Name - Alice and Age - 30.

"""Python return statement"""
def add(a,b):

    #returning sum of a and b
    return a+b

def is_true(a):

    #returning boolean of a
    return bool(a)

#calling functioni
res =  add(2, 3)
print(res)
# -> 5

res = is_true(2<5)
print(res)
# -> True

"""Returning Multiple Values"""

def fun():
    name = 'Alice'
    age = 30
    return name, age

name, age = fun()
print(name)
print(age)

# ALice
# 30

""""Returning List"""
