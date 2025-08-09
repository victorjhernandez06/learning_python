"""
GET LENGTH OF DICTIONARY
"""
# USING LEN() FUNCTION
# This method returns the numbers of keys in dictionary

d= {'name':'Victor', 'age':42, 'city':'Las Vegas - Cojedes'}
print(len(d))
#-> 3

"""
Using a list Comprehesion
"""

d = {'a':1, 'b':2, 'c':3}
length = len([key for key in d])
print (length)

#->3

"""
Using sum() with 1 for each item
"""

d={'a':1,'b':2,'c':3}
length = sum(1 for i in d)
print (length)

# ->3

"""
Getting length of nested dictionary
"""
d = {
    "person1": {"name": "Victor", "age": 42},
    "person2": {"name": "karina", "age": 41},
    "person3": {"name": "Adrian", "age": 16},
    "person4": {"name": "Mathias", "age": 10},
    "person5": {"name": "Sofia", "age": 9}
    }
length = len(d)
print(length)
# -> 5

"""
Using Loop to count items (manual counting)
"""

d = {
    "person1": {"name": "Victor", "age": 42},
    "person2": {"name": "karina", "age": 41},
    "person3": {"name": "Adrian", "age": 16},
    "person4": {"name": "Mathias", "age": 10},
    "person5": {"name": "Sofia", "age": 9}
    }

cnt = 0
#loop through the top-level dictionary
for key, val in d.items():
    if isinstance(val, dict): #check if the value is a nested dictionary
        #loop through the nested dictionary
        for i in val:
            cnt += 1 #Count each key in the nested dictionary
        else:
            cnt += 1 #Count the top-level keys
print (cnt)
# - > 15

# We iterate over each key-value pair in the top-level dictionary d.
# If the value is a nested dictionary (as in the case of person1, person2, person3 ... person5), we loop through that nested dictionary and count its key (name and age)
# we also count the top-level keys (person1...person5).
# The total count of items (keys) in the entire dictionary is 6 (3 top-level-keys + 3 keys inside the nested dictionaries).
# Iteramos sore cada par clave - valor en el diccionario de nivel superior.
# Si el valor es un diccionario anidado, recorremos ese diccionario anidado y contamos sus claves.
# Tambien contamos las claves de nivel superior.
# El recuento total de elementos (claves) en todo el diccionario es de 15, 5 fuera y 10 dentro.


"""
Using  len () to get length of keys, values or items
"""

# We can also use the len() function on the dictionary's keys, values or items to determine the number  of keys, values or  key-values pairs.
d =  {'a':1, 'b':2, 'c':3}
#number of keys
length  = len(d.keys())
print(length)
# -> 3

#number of values
length_values = len(d.values())
print(length_values)
# -> 3

#number of items
length_items = len(d.items())
print(length_items)
#-> 3