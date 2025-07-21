"""Python Arrays"""
#note: Python does not have built-in support for Arrays, but python list can be used instead.

"""Arrays"""
#note: This page shows you how to use LIST as ARRAYS, however, to work with arrays in python, you will have to import a library, like the NumPy library.

#Array are used to store multiples values in one single variable:
#example: Create an array containing car name:

cars = ['Ford', 'Volvo', 'BMW']

"""What is an array?"""
# An array is a special variable, which can hold more than one value
# If you have a list of items (a list of car names, for example), storing the cars in single variable could look this:

car1 = 'Ford'
car2 = 'Volvo'
car3 = 'BMW'

# However, what if you want to loop through the cars and find a specify one? And what if you had not 3 cars, but 300?
# The solution is an array!
# An Array can hold many values under a single name, and you can access the values by referring to an index number.

"""Acces the elements of an Array"""
# You refer to an array element by referring to te index number.
# Example: Get the value of the first array item

x = cars[0]
print(x) #--> Ford

# Modify the value of the list array item.
cars[0]= 'Toyota'
x = cars[0]
print(x) #--> Toyota

#note: tje length of an array is always one more then the highest array index.

"""looping Array Elements"""
#You can use the for in loop in loop through all the elements of an array
# Example: Print each item in the cars array:

for i in cars:
    print(i)

# Toyota
# Volvo
# BMW

"""Adding Array elements"""
#you can use the  append() method to add an element to an array.
# example: add one more element to the cars array:

cars.append("Honda")
print(cars) # --> ['Toyota', 'Volvo', 'BMW', 'Honda']

"""Removing Array Elements"""
# You can use the pop() method to remove an element from the array
# Example: Delete the second element of the cars array:
cars.pop(1)
print(cars) # --> ['Toyota', 'BMW', 'Honda']

#you can also use the remove() method to remove an element from the array.
#Example: Delete the element thar has the value: 'Volvo'
cars.remove("BMW")
print(cars) # --> ['Toyota', 'Honda']