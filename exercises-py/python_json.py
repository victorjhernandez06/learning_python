"""Python JSON"""
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript Object notation.

"""JSON in Python"""
# Python has a built-in package called json, which can be used to work with JSON data.
import json

"""Parse JSON  - Convert from JSON to Python"""
# If you have a JSON strong, you can parse it by using the json.loads() method.
# The result will be Python Dictionary
#Example: convert from JSON to Python.

#some JSON
x = '{"name":"Victor", "age":42,"city":"Las Vegas"}'

#parse x:
y = json.loads(x)

# The result is a python dictionary:
print(y['age']) # --> 42

"""Convert from Python to JSON"""
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# Example: Convert from python to JSON.

# a Python object (dict):
x = {
    "name": "Victor",
    "age": 42,
    "city": "Las Vegas"
}

#convert into JSON
y = json.dumps(x)

# the results is a JSON string
print(y)

# ou can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

# Example: Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name":"victor", "Age":43}))
print(json.dumps(['apple', 'banans']))
print(json.dumps(('apple', 'banana')))
print(json.dumps('Hello'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(False))
print(json.dumps(None))


#when you convert from Python to JSON, python objects are converted into JSON (Javascript) equivalent.

#Python --> JSON
# dict --> Object
# list --> Array
# tuple --> Array
# str --> String
# int --> Number
# int --> Number
# True --> true
# False --> false
# None --> null

# Example: Convert a Python object containing all the legal data types:
import json
x = {
    "name":"Victor",
    "age": 43,
    "Married": True,
    "Divorced": False,
    "Children":("Adrian","Mathias","Sofia"),
    "pets": None,
    "cars": [
        {"model":"BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1},
    ]
}
print(json.dumps(x))

"""Format the result"""
# The example above prints a JSON string, but it is not very easy to read, with indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result.

#Example: use the indent parameter to defien the number of indents:
json.dumps(x, indent=4)

#you can also define the separators, default value is (",",":"), which means using a comma and space to separate each object, and colon and space to separate keys from values:
#Example: Use the separators parameter to change the default separator

json.dumps(x, indent=4, separators=(". ", " = "))

