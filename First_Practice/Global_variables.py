x = "awesome"

def myfunc():
    print("python is " + str(x))

myfunc()

print("Next exercise...")
print()
"""
if  you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, globar and with the original value
"""

x = "awesome"

def myfunc1():
    x = "fantastic"
    print("Print is" + x)

myfunc1()

print("Python is " + x)

# The global keyword

#if you use the global keyword, the variable belongs the global scope:

def myfunc2():
    global x
    x = "Victor"

myfunc2()

print("My name is " + x)


## Also use the global keyword if you want to change a global variable inside a function.

#Example: To change the value of a global variable inside a function, refer  to the variable by using the global keyword.

x = "awesome"

def myfunc3():
    global x
    x = "Karina"

myfunc3()
print ("She name is " + x)


##EXERCISE

x = "Victor"
def myfunc4():
    x = "Karina"
myfunc4()
print("My name is " + x)
