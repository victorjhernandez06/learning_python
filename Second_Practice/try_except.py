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
