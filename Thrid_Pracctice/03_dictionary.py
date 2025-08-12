"""
Diccionary
1.- Data structure that stores the value un Key:Value pairs.
2.- Values can be of any data type and can be duplicated,
 whereas keys can't be repeated and must be immutable
"""
from collections import defaultdict

from pygments.lexer import default

"""
USING DICT()

dict()contructor, provides a simple and direct way to create dictionaries 
using keywords arguments.  
This method is useful defining static-key-value pairs in a clean readable manner.
"""
d =  dict(a=1, b=2, c=3)
print(d)
#-> {'a': 1, 'b': 2, 'c': 3}


my_dictionary = {
    "Alemania": "Berlin",
    "Francia":"Paris",
    "Venezuela":"Caracas",
    "Spain": "Madrid"
}
my_dictionary["Italy"]="Lisboa"
# To fix issues, you can rewrite
my_dictionary["Italy"]="Roma"
# -> Roma
print(my_dictionary["Italy"])
print(my_dictionary)
# {'Alemania': 'Berlin', 'Francia': 'Paris', 'Venezuela': 'Caracas', 'Spain': 'Madrid', 'Italy': 'Roma'}


#Remove Items
#Eliminar elementos
del my_dictionary["Francia"]
print(my_dictionary)
# -> {'Alemania': 'Berlin', 'Venezuela': 'Caracas', 'Spain': 'Madrid', 'Italy': 'Roma'}

data2 = {
    28: "Karina",
    4: "Mathias",
    19: "Sofia",
    30: "Adrian",
    6: "Victor"
}

data3 = {
    1984: "Karina",
    2014: "Mathias",
    2016: "Sofia",
    2008: "Adrian",
    1983: "Victor"
}


#De tupla a diccionario.. Funciona igual con las listas.
# from tuple to dictionary.. it works the same with lists.
my_tuple = ("Spain", "France", "UK", "Germany")
dictionary_2 = {
    my_tuple[0]:"Madrid",
    my_tuple[1]:"Paris",
    my_tuple[2]:"Londres",
    my_tuple[3]:"Berlin"
}
print(dictionary_2)

dictionary_3 = {
    23: "Jordan",
    "name": "Victor",
    "team":"Clippers",
    "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}
}

print(dictionary_3)
print(dictionary_3["anillos"])
print(dictionary_3["anillos"]["temporadas"])

#metodos keys: devuelve las llaves
# Keys Methods: ReturnsKeys from dictionaries
print(dictionary_3.keys())
#-> dict_keys([23, 'name', 'team', 'anillos'])

#metodo values: Devuelve los valores
#Values Methods: Returns values from dictionaries
print(dictionary_3.values())
#-> dict_values(['Jordan', 'Victor', 'Clippers', {'temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}])

#Metodo len: devuelve la longitud del diccionario
#len methods: Returns length from dictionaries
print(len(dictionary_3))
#-> 4

d  = {
    1: "geeks",
    2: "For",
    3: "Geeks"
}
print (d)

#Create diccionary using {}
d1 = {
    1: "geeks",
    2: "For",
    3: "Geeks"
}
print (d1)

#create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for",  c= "Geeks")
print (d2)

""""
1. -from Python 3.7 version onward, python dictionary are ordered.
2. -Dictionary keys are case sensitive
3. -key must be immutable
4. -keys must be unique
5. -dictionary internally uses Hashing. Hence, operations like search, insert
delete can be performend in Constant time

1. -Desde Python 3.7, los diccionarios son ordenados.
2. -Las llaves deben ser inmutables.
3. -Las llaves deben ser unicas.
4. - internamente el diccionario utiliza hash, Por eso, tanto operaciones como buscar, 
eliminar, se pueden realizar en tiempo constante.
"""
#Accesing Dictionary Items
data4 = {
    "Enero1984": "Karina",
    "Octubre": "Mathias",
    "Febrero": "Sofia",
    "Diciembre": "Adrian",
    "Enero1983": "Victor"
}

data5 = {
    "Enero" : {
        1983: "Victor",
        1984: "Karina"
    },
    "Febrero": "Sofia",
    "Octubre": "Mathias",
    "Diciembre": "Adrian"
}

print(data5["Enero"])
print(data5["Enero"][1984])
print(data3[1983])

#ADDING AND UPDATING DICTIONARY ITEMS
d = {1: 'Geeks', 2:'For', 3:'Geeks'}
#Adding a new key-value pair
d['age']=22

#updating an existing value
d[1]= 'Python dict'

print(d)

#REMOVING DICTIONARY ITEMS
# del: remove an item by key
# pop(): removes an item by key and returns its value
# clear(): Empties the dictionary
# popitem*(): Removes and returns the las key-value pair.

# using del to remove item
del d[1]
print (d)
#{2: 'For', 3: 'Geeks', 'age': 22}

#using pop() to remove an item and return the value
val = d.pop(2)
print(val)
# -> For

#using popitem to removes and returns the las key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")
# -> Key: age, Value: 22

# Clear all items from the dictionary
d.clear()
print(d)
# -> {}

"""
PYTHON DICTIONARY kEYS() METHODS
"""
#Python Dictionary keys() method
d = {1: 'Geeks', 2:'For', 3:'Geeks'}
k = d.keys()
print(k)
# -> dict_keys([1, 2, 3])

#EXAMPLE 1
#Iteranting over keys.
for k in data5.keys():
    print(k)
# Enero
# Febrero
# Octubre
# Diciembre

#EXAMPLE 2
#Dymanic nature of Keys()
d = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
k = d.keys()

#adding a new key-value pais to the dictionary
d['D'] = 'Python'
print(k)
# -> dict_keys(['A', 'B', 'C', 'D'])

#Example 3: Using Keys() with list()
d = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
kl = list(d.keys())
print(kl)
#-> ['A', 'B', 'C']

#Removes and return
# inializing dictionary student
student = {"rahul": 7, "aditiya":1, "shubham":4}

#printing original dictionary
print(student)

#using dictionary pop
suspended =  student.pop("rahul")

#checking key of the element
print("Suspended student roll no. = "+ str(suspended))

#Printing list after performing pop()
print("Remaining student" + str(student))

#How to remove value-key pair from dictionay
#You can use the pop() method.

#initializing dictionary
race_rank = {
     "Victor":42,
     "karina":41,
     "Adrian":16,
     "Mathias":10,
     "Sofia":9
}

#Example 1: Pop an element from the dictionary

#initializing dictionary
test_dict = {
     "Victor":42,
     "karina":41,
     "Adrian":16,
     "Mathias":10,
     "Sofia":9
}
#Printing initial dict
print ("The dictionary before deletion: " + str(test_dict))

#using pop to return and remove key-value pair.
pop_ele = test_dict.pop("Victor")

#Printing the value associated to popped key
print("value associated to popped key is:" + str(pop_ele))

#printing dictionary after deletion
print("Dictionary after deletion is: " + str(test_dict))

#-----
#EXAMPLE2 PYTHON DICTIONARY POP() FIRST ELEMENT.

#Initializing dictionary
test_dict = {
     "Victor":42,
     "karina":41,
     "Adrian":16,
     "Mathias":10,
     "Sofia":9
}
#printing initial dict
print("the dictionary before deletion:"+ str(test_dict))

#using pop to return and remove key-value pair.
pop_first = test_dict.pop("karina")

#printing the value associated to popped key
print("Value associated to popped key is:" + str(pop_first))

#Printing dictionary after deletion
print("Dictionary after deletion is: " + str(test_dict))


# Example3
# Pop an element not present from the dictionary

#initializing dictionary
test_dict2 = {
     "Victor":42,
     "karina":41,
     "Adrian":16,
     "Mathias":10,
     "Sofia":9
}

#printing initial dict
print("Dictionary before deletion" + str(test_dict2))

#using pop to return and remove key-value pair provided default
pop_ele =  test_dict2.pop('liss', 5)

#printing the value associated to popped key prints 5
print("Value associated to popped key is:" + str(pop_ele))
#
# #using pop to return and remove key-value piar no provided default
# pop_ele = test_dict2.pop('Liss')
#
# #printing the value associated to popped key KeyError
# print("Value associated to popped key is:" + str(pop_ele))


"""
PYTHON DICTIONARY VALUES() METHODS
"""

d = {
     "Victor":42,
     "karina":41,
     "Adrian":16,
     "Mathias":10,
     "Sofia":9
}

#Using values() to get all values.
v = d.values()
print (v)
# - > dict_values([42, 41, 16, 10, 9])
# Obtenemos los valores de cada clave, en el mismo orden en que se encuentran creados.

# values() syntax => dict.vaues(), este es el objeto values.
# Este metodo devuelve un objeto de vista dict_values.
#this method returns a dict_values view object.

#terating over dictionary values.
d = {"A":"Python", "B":"Javascript", "C":"PHP", "D":"Kotlin"}
#using values() to iterate over dictionary values
for value in d.values():
    print(value)

#-> Output
# Python
# Javascript
# PHP
# Kotlin

#Example2
#Dynamic nature of values()

d = {'A':'Python', 'B':'Java'}
#getting values
values = d.values()

#adding a new key-values pair
d['C']='C++'

print (values)
#-> dict_values(['Python', 'Java', 'C++'])


#Example 3
#converting values() to a list

d = {'A':'Java', 'B':'PHP', 'C':'Kotlin'}
#converting values to a list
values_list = list(d.values())

print(values_list)
# -> ['Java', 'PHP', 'Kotlin']


"""
PYTHON DICTIONARY ITEMS() METHOD.
Returns a view object that contains all the key-value pais in a dictionary as tuples.
"""

d = {"A":"Python", "B":"Javascript", "C":"PHP", "D":"Kotlin"}
#using items() to get all key-value pairs
items = d.items()

print(items)
#-> dict_items([('A', 'Python'), ('B', 'Javascript'), ('C', 'PHP'), ('D', 'Kotlin')])

#items() syntax => dict.items()
#this method does not take any parameters
#return values a dict_items view object, which behaves like of list (key, values) tuples.

# Example 1
# iterating over key-values pairs
d = {"A":"Python", "B":"Javascript", "C":"PHP", "D":"Kotlin"}
#using items() to iterate over dictionary
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

#Output
#Key: A, Value: Python
# Key: B, Value: Javascript
# Key: C, Value: PHP
# Key: D, Value: Kotlin

# Example 2: Dymanic nature of items()
d = {"A":"Python", "B":"Javascript", "C":"PHP", "D":"Kotlin"}
#getting items
items = d.items()

# adding a new key -values
d['E']='C++'

print(items)
#dict_items([('A', 'Python'), ('B', 'Javascript'), ('C', 'PHP'), ('D', 'Kotlin'), ('E', 'C++')])

# Example 3:
# Converting items() to a list
d = {"A":"Python", "B":"Javascript", "C":"PHP", "D":"Kotlin"}
#converting items to a list
items_list = list(d.items())


"""
USING DICTIONARY COMPREHENSION
"""

keys = [ 'a', 'b', 'c']
values = [1, 2, 3]

d = {k: v for k, v in zip (keys, values)}
print(d)
# -> {'a': 1, 'b': 2, 'c': 3}

# Aqui iteramos sobre los pares clave-valor generados por zip(), asignando cada clave a su valor
# respectivo y construyendo el diccionario d.
# here iterate over key-value pairs generated by zip(), assigning each key to its respective
# value and constructing the dictionary d.

"""
USING DICTIONARY 
"""
from collections import defaultdict

a = [('a,1'),('b',2),('c',3),('d',4)]
d =  defaultdict(list) #Create a defaultdict with list as the default value type

# for key, value in a:
#     d[key].append(value)

# print (dict(d))

# for loop iterates through the list a, appending values directly, eliminating the need
# key existence checks. Finally the defautdict is converted to a regulary dictionary
# a traves del buble for, iteramos la lista a, agregando valores directamente, eliminando
# la necesidad de realizar comprobaciones de existencia de claves.



"""
Using setdefault()
"""
# Simplifies dictionary creation by initializing keys with a default value if they don't already exist
# Simplifica la creacion de diccionarios al inicializar claves con un valor predeterminado s un no existen los valores.

a = [('a',1),('b',2),('a',3),('c',4),('a',8)]
d = {}

for key, val in a:
    d.setdefault(key, []).append(val)

print(d)
#-> {'a': [1, 3, 8], 'b': [2], 'c': [4]}
# Agrupa los valores que tienen llaves iguales.

# Explanation:for loop extracts key and val from each tuple in a.
# setdefault(key, []) initializes an empty list for new keys,
# preventing errors and .append(val) then adds values,
# efficiently grouping multiple entries under the same key.

"""
USING FOR LOOP
"""
keys = ['p','q', 'r']
values = [5, 10, 15]

d = {}
for i in range (len(keys)):
    d[keys[i]] = values[i]

print (d)
#-> {'p': 5, 'q': 10, 'r': 15}

#each key from keys is mapped to its corresponding
# value from values using
#cada clave de claves se asigna un valor correspodiente de valores usando d[keys[i]] = values [i]


"""
Python - Add Dictionary Items
"""
# Common operation when you're workin with dynamic data building or  building complex data structures.

"""
ADDING ITEMS USING DIRECT ASSIGNMENT
"""
d= {1:10, 2:20, 3:30}
d[4]=40 #Add a new key-value pair
print(d)

#-> {1: 10, 2: 20, 3: 30, 4: 40}

"""
ADDING MULTIPLE ITEMS USING UPDATE() METHOD.
"""
# This methods accepts dictionary or an iterale of key-value pairs adds those pairs originals dictionary.

d = {1:10, 2:20, 3:30}
a =  [(4, 40), (5, 50)]

d.update(a) # Add items from an iterable.
print(d)
#-> {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

"""
Adding items using setdefault() Method
"""
# This method checks if a key already exists:
    # If the key exists, it return its value.
    # If the key does not exists, it adds the key with a specified default value.

d2 = {1:10, 2:20, 3:30}
d2.setdefault(4,40) # Adds key 4 with value 40.
print(d)

#-> {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}


"""
Adding items using dictionary comprehension
"""

# d1 = {1:10, 2:20, 3:30}
# # Adds items where the key is greater than 2.
# # Agregar elementos donde la clave sea mayor que 2.
#
# d2 = {k:v * 2 for k, v in data.items() if k > 2}
# print(d2)

"""
Adding Items Using a loop.
"""
d1 = {1:10, 2:20, 3:30}
for i in range (4, 6):
    d[i] = i * 10 #add new items in a loop.
print(d)

#-> {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}


"""
PYTHON ACCESS DICTIONARY
"""
#To get or "access" a value stored in a dictionary,
# we need to know the corresponding key
"""
Accesing values in dictionary
"""
# using square brackets [] -> Directly access the value using the key.
# using .get() method -> Access the value using the key with an optional default value.
# Using .values() method -> Retrieve all values as a list-like object (not directly accesing by key)


"""
Using keys inside square brackets []
"""
d1 = {1:10, 2:20, 3:30}
print(d[1])
#-> 10

"""
Using .get() Method
"""
d = {1:10, 2:20, 3:30}
# Access value using get() method
print (d.get(1))
#-> 10
print (d.get(4,'key not found'))
# -> Key not found


"""
Using .values() Method
"""
d = {1:10, 2:20, 3:30}
# Acces all values
print(list(d.values()))
#-> [10, 20, 30]


"""
Accesing Keys in a Dictionary.
"""
d = {'a': 10, 'b': 20, 'c': 30}
# Access all keys
print(list(d.keys()))
# -> ['a', 'b', 'c']

"""
Using a loop
"""
d = { 'a':10, 'b':20, "c":30}
#loop to access keys
for k in d:
    print(k)

# a
# b
# c

"""
Accesing Both Keys an Values
"""
# using .items() method
# using a loop

"""
Using .items() method
"""

d = {'a': 10, 'b':20, 'c':30}
# Access both keys and values
for k, val in d.items():
    print(f"Keys: {k}, Values: {val}")
#-> Outputs
# Keys: a, Values: 10
# Keys: b, Values: 20
# Keys: c, Values: 30


"""
Using a loop
"""

d = {'a': 10, 'b':20, 'c':30}
for k in d:
    print(f"key: {k}, values {d[k]}")
# key: a, values 10
# key: b, values 20
# key: c, values 30


"""
Checking if a key Exists
"""

d = { 'name': 'victor', 'age': 42, 'city': 'las Vegas - Cojedes'}
if 'name' in d:
    print("found!")
else:
    print("not found.")
# -> found!

"""
Nested Dictionary Acces
"""
d = {
    "person": {
        "name": "Alice",
        "age": 25
    },
    "location": {
        "city": "New York",
        "country": "USA"
    }
}

# Accessing nested dictionary values
print(d['person']['name'])
print(d['location']['city'])

# Alice
# New York




