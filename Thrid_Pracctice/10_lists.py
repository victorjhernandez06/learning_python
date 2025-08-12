"""LISTS"""
# the list are used store multiple items in a single variable.
# Lists area created using square brackets []


myList = ["apple","banana","cherry"]
print(myList) # --> ['apple', 'banana', 'cherry']

thisList = ["apple","banana","cherry"]
print(thisList) # --> ['apple', 'banana', 'cherry']

"""List Items"""
# List items are ordered, changeable,and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index[1]...etc.

"""Ordered"""
# when we say that lists are ordered, it means that the items have a defined order, and that order will not change. 
# if you add new items to a list, the new items will be placed at the end of the list.

"""Changeable"""
# the list is changeable, meaning that we can change, add, and remove items in the list after it hass been created.

"""Allow Suplica"""
# Since lists are indexed, lists can have items with the same value
thisList = ["apple","banana","cherry","apple","cherry"]
print(thisList) # --> ["apple","banana","cherry","apple","cherry"]

"""List Length"""
# to determine how many items a list has, use the len() function
print(len(thisList)) #--> 5

"""List items =  data types"""
# List items can be of any data type:
# String, int and boolean data type
list1 = ["apple","banana","cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, True]

# A list can contain different data types
list4 = ["abc",34,True,40.3,"male"]

"""Type()"""
print(type(list4)) # --> <class 'list'>

"""The list constructor"""
theList = list(("apple","banana","cherry")) # note the double round-brackets
print(theList) #-->['apple', 'banana', 'cherry']

""" Access List Items"""
# List items are indexed and you can access them by refering to te index number.
print(thisList[2]) # --> cherry.

"""Negative Indexing"""
# -1 refers to the las item -2, refers to the second las items, etc..
print(thisList[-1]) #--> cherry

"""Range of indexes"""
# you can specify a range of indexes by specifying where to start and where to end the range.
# when specifiying a range, the return value will be a new list with the specified items

thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thisList[2:5]) #--> exclude the las item, start in 2, and finish in 4. 
# --> ['cherry', 'orange', 'kiwi']

# this example returns the items from the beginning to, but NOT including, "kiwi"
print(thisList[:4]) #--> ['apple', 'banana', 'cherry', 'orange']

# By leaving out the end value, the range will go on the end of the list
print(thisList[2:]) #--> ['cherry', 'orange', 'kiwi', 'melon', 'mango']

"""Range of negative indexes"""
# specify negative indexes if you want to start the search the search from the end of the list.
print(thisList[-4:-1]) #--> ['orange', 'kiwi', 'melon']

"""Check if item exists"""
# to determine if specified item is present in a list use the in keyword.
# check if "apple" is present in the list.
thisList = ["apple", "banana","cherry"]
if "apple" in thisList:
    print("yes, 'apple' is in the fruits list") 
    
"""PYTHON - CHANGE LIST ITEMS"""

"""Change item value"""
# To change the value of a specific item, refer to the index number
thisList = ["apple", "banana","cherry"]
thisList[1] = "mango"
print(thisList) # --> ['apple', 'mango', 'cherry']


"""Change a range of item values"""
# To change the value of items withi a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.
thisList=["apple", "banana", "cherry", "orange", "kiwi","mango"]
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList) #--> ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#if you insert more items than you replace , the new items will be insert where you specified, and the remaining items will move accordingly.
thisList = ["apple","banana","cherry"]
thisList[1:2] = ["blackcurrant","watermelon"]
print(thisList) # --> ['apple', 'blackcurrant', 'watermelon', 'cherry']

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# if you insert less items than you replace, the new items will be inserted where you specified, and the remaining items move accordingly

thisList = ["apple","banana","cherry"]
thisList[1:3] = ["watermelon"] #aqui elegimos insertar watermelon en los espacios del 1 al 2, por lo que la lista queda recortada  y solo imprime: ['apple', 'watermelon']
print(thisList) #--> ['apple', 'watermelon']

"""INSERT ITEMS"""

# to inser a new list item, without replacing any of the existing values, we can use teh insert()method inserts an tiem at the specified index.


"""PYTHON ADD LIST ITMES"""

"""APPEND ITEMS"""
# to add a item to the end the list, use the append() method.

thisList = ["apple","banana","cherry"]
theList.append("orange")
print(theList) #--> ['apple', 'banana', 'cherry', 'orange']

"""INSERT ITEMS"""
# To insert a list items at a specified index, use the insert() method. this inserts an items at the specified index.

theList = ["apple","banana","cherry"]
theList.insert(0, "orange")
print(theList) #--> ['orange', 'apple', 'banana', 'cherry']

"""EXTEND LIST"""
# to append elements from another list to the current list, use the extend() method.
thisList = ["apple","banana","cherry"]
tropical = ["mango","pineaple", "papaya"]
thisList.extend(tropical)
print(thisList) #--> ['apple', 'banana', 'cherry', 'mango', 'pineaple', 'papaya']

"""ADD ANY ITERABLE"""  
# The extend() method does not have to apppend lists, you can add any iterable object (tuples, sets, dictionaries, etc).

# Add elements of a tuple to a list.
thisList = ["apple","banana","cherry"]
thistuple = ["kiwi","orange"]
thisList.extend(thistuple)
print(thisList) #--> ['apple', 'banana', 'cherry', 'kiwi', 'orange']


"""PYTHON REMOVE LIST ITEMS"""

"""REMOVE SPECIFIED ITEM"""
# The remove() method removes the specified item.
# Remove "banana"

thisList = ["apple","banana","cherry"]
thisList.remove("banana")
print(thisList) #--> ['apple', 'cherry']

# if there more than item with the specified value, the remove() method removes the first occurrence
thisList = ['apple','banana','cherry','banana','kiwi']
thisList.remove("banana")
print(thisList) #--> ['apple', 'cherry', 'banana', 'kiwi']

"""REMOVE SPECIFIED INDEX"""

# the pop() method removes the specified index.
thisList=['apple','banana','cherry']
thisList.pop(1)
print(thisList) #--> ['apple', 'cherry']

# if you do not specify the index, the pop() method removes the last item.
theList.pop()
print(theList) #--> ['apple']

# the del keyword also removes the specified index
thisList = ['apple','banana','cherry']
del thisList[0]
print(thisList) #--> ['banana', 'cherry']

# The del keyword can also delete the lis completely
thisList = ['apple','banana','cherry']
del thisList
#--> if you print(thisList)  --> NameError: name 'thisList' is not defined

"""CLEAR THE LIST"""
# The clear() method empties the list.
# the list still remains, but it has no content.
thisList = ["apple","banana","cherry"]
thisList.clear()
print(thisList) #--> []

"""PYTHON LOOP LISTS"""

"""LOOP THROUGH A LIST"""
# You can loop through the list items by using a for loop.
# print all items in the list, one by one.
thisList = ["apple","banana","cherry"]
for x in thisList:
    print(x) 
# apple
# banana
# cherry

"""LOOP THROUGH THE INDEX NUMBERS"""
# you can also loop through the list items by refering to their index number.
# use the range() and len() functions to create a suitable iterable

thisList = ["apple","banana","cherry"]
for i in range(len(thisList)):
    print(thisList[i])

# -> The iterable created in the example above is [0, 1, 2]
# apple
# banana
# cherry

"""USING A WHILE LOOP"""
# You can loop through the list items by using a while loop
# Use  the len() function to determine the length of the list, the start at 0 and loop way through the list items by refering to their indexes.
# Remember to increase the index by  after each iteraction.

#print all items using a while lopp to go through all the index numbers.

thisList = ["apple","banana","cherry"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1
# apple
# banana
# cherry


"LOOPING USING LIST COMPREHENSION"
#  list comprehension offers a shorter syntax for looping through list.
#  A short hand for loop that will print all items in a list.
thisList = ["apple","banana","cherry"]
[print(x) for x in thisList]
# apple
# banana
# cherry

"""PYTHON LIST COMPREHENSION"""
# List comprehension offers a shorter syntax when you want to create a new list based on values of an existing list.

# Example, Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#  Without list comprehension you have to write a for statement with a conditional test inside.

fruits = ["apple","banana","cherry","kiwi","mango"]
newList = []
for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList) #--> ['apple', 'banana', 'mango']

print("---------------")
fruits = ["apple","banana","cherry","kiwi","mango"]
newList = []
for x in fruits:
    if "e" in x:
        newList.append(x)
print(newList)

# with list comprehension you can do all that with only one line of code

fruits = ["apple","banana","cherry","kiwi","mango"]
newList = [x for x in fruits if "a" in x]
print(newList)

# The syntax 
# newList = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old unchanged

# Condition
# the condition is like a filter that only accepts the items that evaluate to True.
# Only accept items that are not "apple"

newList = [x for x in fruits if x != "apple"]

# The condition if x != "apple" will return True for all elements other than "apple", making the new list contain all fruits except "apple"
# the condition is optional and can be omitted:
# With no if statement

newList = [x for x in fruits]
print(newList) #--> ['apple', 'banana', 'cherry', 'kiwi', 'mango']

"""ITERABLE"""
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable.
newList = [x for x in range(10)]
print(newList) #--> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# accept only numbers lower than 5:
newList = [x for x in range(10) if x < 5]
print(newList) #--> [0, 1, 2, 3, 4]

"""EXPRESSION"""

# The expression is the current item in the iteration, but it is also the outcome which you can manipulate before it ends up like a list item in the new list.

# Set the values in the new list to upper case:
newList = [x.upper() for x in fruits]
print(newList) #--> ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# you can set outcome to whatever you like 
# Set all values in the new list to "hello"
newList = ["hello" for x in fruits]
print(newList) #--> ['hello', 'hello', 'hello', 'hello', 'hello']

# The expression can also contain conditions, not like filter, but as a way to manipulate the outcome
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newList = [x if x != "banana" else "orange" for x in fruits]
print(newList) #--> ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# Exercise
fruits = ["apple", "banana","cherry"]
newList = [x for x in fruits if x == "banana" ]
print(newList) #--> ['banana']

"""PYTHON SORT LIST"""

"""Sort list  alphanumerically"""
# list objects have sort() method that will sort the list alphanumerically ascending, by default

theList = ["orange","mango","kiwi","pineaple","banana"]
theList.sort()
print(theList) # -->  ['banana', 'kiwi', 'mango', 'orange', 'pineaple']

# sort the list numerically
thisList = [100, 50, 65, 82, 34]
thisList.sort()
print(thisList) #--> [34, 50, 65, 82, 100]


"""SORT DESCENDING"""
#sort the list descending
thisList = ["orange", "mango","kiwi","pineaple", "banana"]
thisList.sort(reverse=True)

# sort the list descending
thisList = [100, 50, 60, 82, 23]
thisList.sort(reverse=True)
print(thisList)

"""CUSTOMIZE SORT FUNCTION"""
# You can also customize your own function by using the keyword argument key = function
# The function will return a number that will be used to sort the list (the lowest number first)

# Example
# Sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n -50)

thisList = [100, 50, 65, 82, 23]
thisList.sort(key = myfunc)
print(thisList) #--> [50, 65, 23, 82, 100]

"""CASE INSENSITIVE SORT"""
# By default the sort() method is case sensitive, resulting in all capital letters
thisList = ["banana","Orange","Kiwi","cherry"]
thisList.sort()
print(thisList) #--> ['Kiwi', 'Orange', 'banana', 'cherry']

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-sensitive sort function, use str.lower as a key function.

# Example.
# Perfom a case-sensitive sort of the list.
thisList = ["banana","Orange","Kiwi","cherry"]
print(thisList) # --> ['banana', 'Orange', 'Kiwi', 'cherry']

"""REVERSE ORDER"""
# What if you want to reverse the order of a list, regardless of the alphabet.
# The reverse() method reverses the current sorting order of the elements. 

# Reverse the order of the list items.
thisList = ["banana","Orange","Kiwi","cherry"]
thisList.reverse()
print(thisList) #--> ['cherry', 'Kiwi', 'Orange', 'banana']

"""Python - Copy Lists"""
# You cannot copy a list simply by tiping list1 = list2, because list2, will only be a reference to list1, and changees made in list1 automatically also be made in list2

"""Use the copy() method"""
# You can use the build-in List Method copy() to copy a list.

thisList = ["Object1","Object2","Object3"]
myList = thisList.copy()
print(myList) # --> ['Object1', 'Object2', 'Object3']

"""Use the list() Method"""
# Another way to make a copy is to use the built-in method list().

thisList = ["Object1","Object2","Object3"]
myList = list(thisList)
print(myList) #--> ['Object1', 'Object2', 'Object3']

"""Use the slice operator"""
# You ca also make a copy of a list by using the : (slice) operator.
thisList = ["Object1","Object2","Object3"]
myList = thisList[:]
print(thisList) #--> ['Object1', 'Object2', 'Object3']

"""Pyhton two List"""
# There are several ways to join, or concatenate two or more list in Python.
# One of the easiest ways by using the + operator.

list1 = ["a","b","c"]
list2 = [19,32,21]

list3 = list1 + list2
print(list3) # --> ['a', 'b', 'c', 19, 32, 21]
list3 = [str(x) for x in list3]
print(list3, "--")

string = [x for x in list3 if isinstance(x, str)]
numbers = [x for x in list3 if isinstance(x, int)]

string.sort()
numbers.sort()

list3_sorted = string + numbers
print(list3_sorted)

list1.sort() #Ordeno la lista1
list2.sort() # Ordeno la lista2
list3 = list2 + list1 #luego puedo unir las listas, de la manera que vea conveniente.
print(list3)
list3 = list1 + list2 #Aqui hay otra manera de ordenar las listas.
print(list3)

# Ordenando las listas a un solo tipo de dato
list3 = [str(x) for x in list3]
list3.sort()

print(list3) #--> ['19', '21', '32', 'a', 'b', 'c']

# Podemos convertir todo a int (Solo si es posible)
list1 = ["1","5","3"]
list2 = [18, 7, 32]

list3 = list1 + list2
# convertimos todos a int
list3 = [int(x) for x in list3]
list3.sort()

print(list3) #--> [1, 3, 5, 7, 18, 32]

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 =list1 + list2
print(list3) 

# Or you can use the extend() method, where the purpose is ti add elements from one list to another list.
list1 = ['a','b','c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

"""PYTHON JOIN LISTS"""
# Join two lists
# there are several ways to join, or concatenate, two or more lists in python.
#  One of the easiest ways are by using the + operator.

list1 = ['a','b','c']
list2 = [1, 2, 3]
list3 = list2 + list1
print(list3) #--> [1, 2, 3, 'a', 'b', 'c']

# Another way to join two lists is by appening all the items from list2 into list 1, one by one

list1 =["medicina1","medidicina2","medicina3"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1) # --> ['medicina1', 'medidicina2', 'medicina3', 1, 2, 3]

# You can use the extend() method, where the purpose is to add elements from one list to another list.

list1 = ['step1','step2','step3']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)#--> ['step1', 'step2', 'step3', 1, 2, 3]