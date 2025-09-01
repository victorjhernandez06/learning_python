# The try block lets yoy test a block of code for errors.
# The except block lets you handle the error
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try-and except blocks

"""Exception Handling"""
# When an errors occurs, or exception as we call it, Python will normally stop and generate an error message.
# THese exceptions can be handled using the try statement.

#Example
# The try block will generate an exception, because x is not defined.
try:
    print(x)
except:
    print("An Exception Ocurred_1")

# since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error.

# Example: this statement will raise an error, because x is not defined:
# print(x)

"""Many exceptions"""
# Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

"""ELSE"""

# You can use the else keywords to define a block of code to be executed if no errors were raised.

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

"""FINALLY"""
# The finally block, iff specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")

# This can be useful to close objects and clean up resources:

# Example: Try to open and write too a ile that is not writable
try:
    f = open("demofile.txt")
    try:
        f.write("Lorem ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# This can be useful to close objects and clean up resources:

# Example: try to open and write to a file tha is not writable
try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrogn when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file_1")

"""Raise an exception"""
# As a Python developer you can choose tho throw an exception ig condition occurs.
# To throw (or raise) an exception, use the raise keyword.
#Example: Raise an error and stop the program if x is lower than 0:

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
#Example: Raise a TypeWError if x is not an integer.
x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
