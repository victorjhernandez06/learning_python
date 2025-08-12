import math

"""
###DICTIONARIES
Are sometimes found in other languages as "associative memories" or "associative arrays". Unlikes sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; string and numbers can always be keys. Tuples can be used as keys if contain only string, numbers or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can't use list as keys, since list can be modified in place using index assignments, slice assignments, or methods like append() an extended()

it is best to think of a dictionary as a set of key: value pairs, with the requirement that keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial keys:value pairs to the dictionary, this also the way dictionaries are written on output.

the main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pairs with del. If you store using a key that is already in use, the old value associated with that key is forgotten. it is an error to extract a value  using a non-existent key.

Performing list (d) on a dictionary returns a list of all key used in dictionary, in insertion order (if you want it sorted jus use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.
"""

tel =  {'Jack': 4098, 'aspe':4125}
tel['guido']=4127 #add key:valor pairs
print (tel) #--> {'Jack': 4098, 'aspe': 4125, 'guido': 4127}

print(tel ['Jack']) #--> 4098
tel['irv']=4127
print(tel) #--> {'Jack': 4098, 'aspe': 4125, 'guido': 4127, 'irv': 4127}

del tel['aspe']
print(tel) #--> {'Jack': 4098, 'guido': 4127, 'irv': 4127}

list(tel)
print(list(tel)) #--> ['Jack', 'guido', 'irv']
print(type(list(tel))) #--> <class 'list'>
print(sorted(tel)) #--> ['Jack', 'guido', 'irv']

print('guido' in tel) # --> True
print("victor" in tel) #--> False

# The dict() constructor builds dictionaries directly from sequences of key:value pairs.

print(dict([('sape', 4139), ('guido', 4127),('Jack', 4098)])) #--> {'sape': 4139, 'guido': 4127, 'Jack': 4098}

# In additio, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions.
print({x:x**2 for x in {2,4,6}}) #--> {2: 4, 4: 16, 6: 36}, es decir cuando indicamos que la key vale 2, su valor se eleva al cuadrado y da como resultado 4 (2*2), si key=4, valor=16(4*4)


# when the keys are simple strings, it is sometimes easier to specify pairs using keywords arguments
print(dict(sape=4139, guido=4127, jack= 4099)) #--> {'sape': 4139, 'guido': 4127, 'jack': 4099}


""" LOOPING TECHNIQUES """
#  whn looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

knights = {'Gallahand': 'the pure', 'Robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Gallahand the pure
# Robin the brave

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate()

for i, v in enumerate(['tic', 'tic', 'tic']):
    print(i, v)

# 0 tic
# 1 tic
# 2 tic

# To loop over two or mmore sequence at the same time, the entries can be with the zip() function

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('Whats is your {0}? It is {1}.'.format(q,a))

# Whats is your name? It is lancelot.
# Whats is your quest? It is the holy grail.
# Whats is your favorite color? It is blue.

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered

basket = ['apple', 'orange', 'apple','pear','orange','banana']
for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

print('------')
# Using set() on an sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorteed order.


basket = ['apple', 'orange', 'apple','pear','orange','banana']
for f in sorted(set(basket)):
    print(f)
# apple
# banana
# orange
# pear

# It is sometimes tempting to change a list while you are looping over it, however, it is often simpler and safer to create a new list instead


raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
#--> [56.2, 51.7, 55.3, 52.5, 47.8]




"""Operaciones con diccionarios"""
my_dict =  dict()
my_other_dict = {}
print(type(my_other_dict)) #--><class 'dict'>
print(type(my_dict)) #--><class 'dict'>

my_other_dict = {'nombre': "brais", "apellido": "moure", "edad":35, 1:"python"}

my_dict = {
    "name":"Victor",
    "Last_name":  "Hernandez",
    "Age": 42,
    "languages":{"python",'Swift',"Kotlin"}
}

my_dict['country'] = 'Venezuela'
print(my_dict) #--> {'name': 'Victor', 'Last_name': 'Hernandez', 'Age': 42, 'languages': {'Kotlin', 'Swift', 'python'}, 'country': 'Venezuela'}
print(my_dict['country']) #--> Venezuela
print("name" in my_dict) # --> True
print("nombre" in my_dict) # -->False

# A dictionary is a data structure that stores key:Values pairs
# data_dictionary = {'clave' : 'valor'}

data_dictionary_one = {'name': 'Victor Hernandez', 'age':45, 'city': 'Cojedes'}

# Acceder a los valores mediante claves
# Access values via key.
print(data_dictionary_one['name']) # --> Victor Hernandez
print(my_other_dict)

#Agregar Elementos
# Add Elements

print('victor' in my_other_dict) #--> False aqui comprueba si la clave 'victor' existe en el diccionario.

print(my_dict.items()) # Retorna todos los valores, ordenados, clave:valor
print(my_dict.keys()) # Retorna todas las claves o keys
print(my_dict.values()) # Retorna todos los valores del diccionario. 

my_new_dict = my_other_dict.fromkeys(("name",1,"address","zip_code"))
print(my_new_dict)
my_new_dict['name']="Mathias"
my_new_dict[1]= "58424"
my_new_dict['address']="Las vegas"
my_new_dict['zip_code']=2204
print(my_new_dict)


# Add many keys:valor one by key

my_dictionary = {'a':1, 'b':2}
my_dictionary['c']=3
my_dictionary['d']=4

print(my_dictionary)

# Add one or more parameters with update() 

my_dictionary.update({"e":5, "f":6, "g":7})
print(my_dictionary)

#  Si quieres que una clave tenga múltiples valores → usa una lista
my_dictionary2 = {"fruit":["apples", "pears"]}

# add more items to the list.
my_dictionary2["fruit"].append("orange")
my_dictionary2["fruit"].extend(["banana","kiwi",'grapes'])
print(my_dictionary2)


# Si quieres que la clave tenga multiples valores, -> defaultdict(optional)
from collections import defaultdict
my_dictionary2 = defaultdict(list)
my_dictionary2["colors"].append('red')
my_dictionary2["colors"].append("green")

print(my_dictionary2)


'''PYTHON DICTIONARY METHODS'''

# Create a dictionary with 3 keys, all with the value 0
x = ('key1', 'key2','key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict) #--> {'key1': 0, 'key2': 0, 'key3': 0}

""" The fromkeys() method returns a dictionary with the specified keys and the specified value.
#  Syntax
#  dict.fromkeys(keys, value)
"""
# Keys Required. An iterable specifying the keys of the new dictionary
# Value Optional. The value for all key. Defaults value is none. 

x = ('key1', 'key2', 'key3')

thisdict_1 = dict.fromkeys(x)
print(thisdict_1) #--> {'key1': None, 'key2': None, 'key3': None}

"""GET() METHODS"""
# The get() method returns the value of the item with specified key.
#  dictionary.get(keyname, value)

car = {
    "brand":"Ford",
    "model":"Munstang",
    "year" : 1964
}

x = car.get("model")
print(x) #--> Mustang
x = car["model"]
print(x) #--> Mustang
print(car["model"]) #--> Mustang

# Try to return the value of an item that do not exist:
car2 = {
    "brand": "ford",
    "model":"350",
    "year":1964
}

x = car.get("Price",15000)
print(x)

my_list1 = ['name', 1, 'piso']
my_new_dict1 = dict.fromkeys(my_list1)
print(my_new_dict1) # --> {'name': None, 1: None, 'piso': None}

my_new_dict1 = dict.fromkeys(("nombre", 1 , "piso"))
print(my_new_dict1) # --> {'nombre': None, 1: None, 'piso': None}

my_new_dict1 = dict.fromkeys(my_dict)
print(my_new_dict1) #--> {'name': None, 'Last_name': None, 'Age': None, 'languages': None, 'country': None}

my_new_dict1 = dict.fromkeys(my_dict, "victor")
print(my_new_dict1) #-> {'name': 'victor', 'Last_name': 'victor', 'Age': 'victor', 'languages': 'victor', 'country': 'victor'}

print(list(my_new_dict1)) #--> ['name', 'Last_name', 'Age', 'languages', 'country']
print(tuple(my_new_dict1)) #--> ('name', 'Last_name', 'Age', 'languages', 'country')
print(set(my_new_dict1)) #--> {'Age', 'Last_name', 'languages', 'country', 'name'}


"""PYTHON DICTIONARY VALUES() METHOD"""
#Ahora si hacemos un punto .values(), nos retorna la variable.
# Returns a list of all the values in the dictionary
car= {
    "brand" : "Toyota",
    "model": "Camry",
    "year":2020
}
x =  car.values()
print(x) #--> dict_values(['Toyota', 'Camry', 2020])

# example 2
car = {
    "brand":"BMW",
    "model": "Mercedes",
    "year": 2024
}
x = car.values()
car['year']= 2018

print(x) #--> dict_values(['BMW', 'Mercedes', 2018])

print('--------------')

my_values  = my_new_dict1.values()
print (type(my_values)) #--> <class 'dict_values'>


print(list(my_new_dict1)) 
print(tuple(my_new_dict1)) 
print(set(my_new_dict1))