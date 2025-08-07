
###FUNCTIONS###
# A function is a block of code wich only runs when it is called.
# You can pass data, know as parameters, into a function.
# A function can return data as a result.

"""Create a function"""
# in python a function is defined using a def keyword.
# Example
from datetime import datetime


def my_function():
    print('A new function example')
    
"""Call a function"""
# to call a function, use the function name followed by parenthesis
my_function()

"""Arguments"""
# information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a fucntion with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
    print(fname + " Hernandez")
  
my_function('Victor') #--> Victor Hernandez
# my_function('Karina')
my_function('Adrian') #--> Adrian Hernandez
my_function('Mathias') #--> Mathias Hernandez
my_function('Sofia') #--> Sofia Hernandez  

# Arguments are often shortened to args in Python documentations.

""" Parameters or Arguments """

# The terms parameter and argument can be used for the same thing: information that are passed into a function.

## From a function perspective: 
# A parameter is the variable listed inside the parentheses in the function definition.
# An Arguments is the value that is sent to the function  when it is called.

"""Number of arguments"""
# by default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have call the function with 2 arguments, not more, and not less.

#example
# this function expects 2 arguments, and gets 2 arguments
def m_function(fname, lname):
    print(fname +" "+ lname)
    
m_function('Karina','Jimenez') #--> Karina Jimenez

# If you try call the fucntion with 1 or 3 arguments, you will get an error:

"""Arbitrary Arguments, *args"""
#if you do not know how many arguments that will be passed into your function, add a asterisk  * before the parameter name in the function definition  
# this way the function will receive a tuple arguments, and can access the items accordingly

#Example
# if the number of arguments is unknown, add a * before the parameter name
def my_function(*kids):
    print(f"The youngest child is {kids[2]}")

my_function('Adrian', 'Mathias','Sofia')

# Arbitrary Arguments are often shortened to *args in Python documentations.

"""Keywords Arguments"""
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter

def my_function(child2, child3, child1):
    print(f'The youngest child is {child3}')

my_function(child2 = 'Mathias', child3 = 'Sofia', child1 = 'Adrian' )
# --> The youngest child is Sofia
# the phrase Keyword Arguments are often shortened to kwagars in Python documentations.

"""Arbitrary Keyword Arguments, **Kwargs"""
# If you do not know how many keywords arguments that will be passed into your function, add two asterisk ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items according.

#Example
# if the number of keywords arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
    print("His last name is " + kid["fname"])
my_function(fname="mathias", lname = "sofia")

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

"""Default Parameter Valuey"""
# The followinfg example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def my_function(country = 'Cojedes'):
    print('I am from '+ country)

my_function('las Vegas') # -->I am from las Vegas
my_function('San Carlos') # --> I am from San Carlos
my_function() # --> I am from Cojedes
my_function('San Miguel I') #--> I am from San Miguel I

"""Passing a List as an Argument"""
# You can send any data types of arguments to a function (string, number, booleans, list, dict, sets, tuples), and it will treated as the same data type inside the function.

# E.g if you send a List a argument, it will still be a list when it reaches the function.

#Example
def my_function(food):
    for x in food:
        print(x)
fruits = ['apple','banana','cherry']

my_function(fruits)
# apple
# banana
# cherry

"""Return Values"""
def my_function(x):
    return 5 * x
print(my_function(3)) #--> 15
print(my_function(5)) #--> 25
print(my_function(9)) #--> 45

"""The pass statements"""
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def my_function():
    pass

"""Positional-Only Arguments"""
# You can specify that a function can have ONLY positiional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments.
def my_function(x,/):
    print(x)
my_function(3)
# Without the ,/ you are actually allowed to use keyword arguments even if the function expects positional arguments.

#Example
def my_function(x):
    print(x)
my_function(x = 3) #--> 3

"""Key-Only Arguments"""
# To specify that a function can have only keyword arguments, add *, before the argument:
#example
def my_function(*, x):
    print(x)
my_function(x = 3) #--> 3

# Without the *. you are allowed to use positional arguments even if the function expects keyword arguments
def my_function(x):
    print(x)
my_function(3)

"""Combine Positional-Only and keyword-Only"""
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *,, are keyword-only.

def my_function(a, b, /, *, c, d):
    print(a+b+c+d)
my_function(5, 6, c = 7, d = 8)


"""Recursion"""
# Python also acepts function recursion, which means a defined function can call itself.
# Recursion iss a common mathematical and programming concept. It means that a function call itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that have defined to call itself("recurse"). We use the k variable as the data, which decrements(-1) every time we recurse. The recursion ends whens the condition is no greater tha 0(i.e when it is 0).

#Example
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k -1)
        print(result)
    else:
        result=0
    return result

print("Recursion example results:")
tri_recursion(7)
# 1
# 3
# 6
# 10
# 15
# 21
# 28




    
# # Exercises (simple)
# def my_function():
#     print('this is a function')
    
# my_function() #Esta es la llamada a la funcion, con esto aparece en pantalla: 'esto es una funcion'


# def sum_two_values (first_num,  second_num):
#     print(first_num + second_num) #hace una suma entre dos parametros.
    
# sum_two_values(23, 21) #ejecuta la funcion e imprime la suma dentro de la funcion.

# def sum_a_b (a, b):
#     return(a+b)

# print(sum_a_b(2,2)) #  --> devuelve e imprime la suma de 2+2 = 4
# print(sum_a_b(1.4,22.8)) # --> 24.2 


# # Al tipado no funciona aqui.
# # Aqui he tipado el numero, pero al indicar que son string los datos, no toma en cuenta este tipado. NO sirve de nada por el tiempo de ejecucion, pues tomara los datos que le metamos datos. 
# def function_2(numb1:int, numb2:int): #aqui probamos tipando los parametros
#     return(numb1+numb2)
# print(function_2('22','20'))

# ###
# def sum_two_val (a, b):
#     return(a + b)

# my_result = sum_two_val(2,3)
# print(my_result) #-->5

# ### Usando el retorn 
# def sum1(a,b):
#     my_sum = a + b
#     return my_sum

# operation = sum1(2,32)
# print(operation) #--> 34

# def print_name(name, surname):
#     print(f"{name} {surname}")

# print_name('Victor','Hernandez') #--> Victor Hernandez
# print_name(surname="Hernandez",name='Victor') #aqui reordene el nombre, indicando el valor de los parametros en la llamada. ##--> Victor Hernandez


# ### Aqui utilizamos parametros definidos dentro de la funcion, sin usar el constructor.
# def print_name_with_default(name,surname, alias = 'Sin Alias'):
#     print(f"{name} {surname} {alias}")
    
# print_name_with_default('Victor','Hernandez','Victordev06') #--> Victor Hernandez Victordev06
# print_name_with_default('Victor','Hernandez') #--> Victor Hernandez Sin Alias

# ### el asterico indica que puedo incluir muchos parametros del mismo tipo
# def print_texts(*text):
#     print(text)
    
# print_texts('Hola')# --> ('Hola',)


# ### El asteristo * indica que es una funcion con parametros arbitrarios
# def print_texts(*texts):
#     for text in texts:
#         print(text.upper())

# print_texts('Victor','Karina','Adrian','Mathias','Sofia')
# # VICTOR
# # KARINA
# # ADRIAN
# # MATHIAS
# # SOFIA

# """MICROSOFT PYTHON """

# def print_time():
#     print('task completed')
#     print(datetime.datetime.now())
#     print()

# first_name  = 'Victor'
# print_time()

# for x in range(0,10):
#     print(x)

 


