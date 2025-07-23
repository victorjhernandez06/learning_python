"""Modules"""


"""Whats is a module"""

# consider a module to be the same as clde library.
# A file containing a set of functions you want to include in your application.

"""Create a Module"""
# To create a module just save the code you want in a file with the file extension .py

"""Use a module"""
# Now we can use the module we just created, by using the import statement.

#Example: import the module named mymodule and call the greeting function.

import mymodule 
mymodule.greeting('Victor', 'Hernandez') # --> Hello Victor Hernandez

"""Variables in module"""
# Save this code in the mymodule.py

a = mymodule.person1["age"]
print(a) #--> 42

"""Naming a Module"""
#you can name the module file wherever you like, but it must have the file extension .py

"""Re-naming a module"""
# you can create en alias when you import a module, by using the as keyword.

# Example: Create an alias for mymodule called mx

import mymodule as mx # --> aqui cambiamos el nombre del modulo.

a = mx.person1['age']
print (a)

