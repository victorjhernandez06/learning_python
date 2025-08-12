"""Python Scope"""
# A variable is only available from inside the region it is created. this is called scope.

"""Local Scope"""
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# Example: a variable created inside a function is available inside that function.
def myfunction():
    x = 300
    print(x)

myfunction() #-->300

"""Function inside function"""
# as explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

# Example:
# The local variable can be accessed from a function within the function:
def myfunction():
    x =430
    def myinnerfunction():
        print(x)
    myinnerfunction() # call the function inside and print the valor.

myfunction() # --> 430

"""Global Scope"""
# A variable created in the main body of the python code is a global variable and belongs to the global scope
# Global variable are available from within any scope, global scope and local.

x = 332
def myfunc1():
    print(x)
myfunc1() # --> 332
print(x) # --> 332


"""Naming Variables"""
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function)
#  Example: The function will print the local x, and then the code will print the global x

x = 653
def myfucn2():
    x = 233
    print(x)
myfucn2() # --> 233 variable inside the function
print(x) # --> 453 outside variable

"""Global keyword"""
# If you need to create a global variable, but are stucj in the local scope, you can use the global keyword.
# THe global keyword makes the variable global.
# Example: If you use the global keyword, the variable belongs to the global scope:
def myfunc3():
    global x
    x = 323
myfunc3()
print(x)

# Also, use the global kkeyword if you want to make a change to a global variable inside a function.
#Example: To change the value of a global variable inside a function, refer to the variable by using the global keyword.
x = 222

def myfunc4():
    global x
    x = 333

myfunc4()
print(x) #--> 333

"""NOnLocal Keyword"""
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

def myfunc5():
    x = "jane"
    def myfunc6():
        nonlocal x
        x = 'Hello'
    myfunc6()
    return x
print(myfunc5()) #--> Hello

