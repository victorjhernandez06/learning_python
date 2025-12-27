"""Python None"""
#None is a special constant in  Python that represents the absence of a value.
# None es una constante especial en Python y representa la ausencia de un valor.

#Its data type is NoneType, and None is the instance of a NoneType object.

# NoneType
# Variables can be assigned None to indicate "no value" or "not set"

#assign and display a None value:

x = None
print(x)

#Use type() to see the type of a None value.
# Assign and print the data type of a None value.
x = None
print(type(x))

""" Comparing to None"""
# TO compare a value to None, use the identity operator is or is not

# Example
# Use the identity operator is for comparisons with None:

result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

#Example
# Similar example, but using is not instead:
result = None
if result is not None:
    print("Result is ready")
else:
    print("No result yet")

"""True or False"""
# None evaluates to False in boolean context.
# Check truthiness:

print(bool(True))

""" Functions returning None"""
# Functions that do not explicitly return a value return None by default.
# A function without a return statement returns None:

def myfunc():
    x = 5

x = myfunc()
print(x)
