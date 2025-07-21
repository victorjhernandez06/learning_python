"""
###SETS
A sets is an unordered collection with no duplicate elements. Basic uses include membershipp testing and eliminating duplicates entries. Set objects also support mathematical operation like union, intersection, difference and symmetric difference

Curly braces or the set() function can be used to create sets. Note: to create an ampty set you have to use set(), not {}; the latter creates an empty dictionary.

# Un Set no es una estructura ordenada, es decir no guarda los datos de manera ordenada, sino desordenada.
# Un set no admite elementos repetidos, puedes añadirlo, pero no lo va a guardar.
# No es inmutable, es decir que puedo agregar mas elementos o datos.
# no podemos acceder a los elementos por via index. [0], tal como hacemos en las listas y en las tuplas.

"""
basket = {'Apple','orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #show the duplicates have been removed

print( 'orange' in basket ) # fast membership testing
print('crabgrass' in basket)

#Demostrate set operations on unique letters from two words
a = set('abracadabra')
b = set('Alacazam')
print (a) # --> {'d', 'r', 'b', 'a', 'c'}
print(a - b) # -->  {'d', 'b', 'r'}
print (a | b) # --> {'d', 'r', 'z', 'b', 'm', 'a', 'A', 'l', 'c'}
print( a & b) # --> {'c', 'a'}
print (a ^ b) # --> {'r', 'z', 'b', 'm', 'A', 'l', 'd'}

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # --> {'d', 'r'}


my_set = set()
my_other_set = {}

print(type(my_set)) # --> <class 'set'>
print(type(my_other_set)) # --> <class 'dict'>

my_other_set = {"Victor", "hernandez", 42}
# Al colocar varios datos en el diccionario, lo transformamos en diccionario. El lenguaje lo interpreta.


# podemos comprobar el tipo de datos
print(type(my_other_set)) # --> <class 'set'>
#podemos ver la longitud del set
print(len(my_other_set)) #--> 3 elements

#agregar un elemento, usando .add, nota: no admite items repetidos, no los va a guardar
my_other_set.add("fenixlogan1")
print(my_other_set) # --> {'hernandez', 42, 'fenixlogan1', 'Victor'}
#elemento no adminito por ser repetido.
my_other_set.add("fenixlogan1")
print(my_other_set)

#Comprobacion de elementos dentro de un sets
print('Victor' in my_other_set) # --> True
print("Jimenez"in my_other_set) # --> False, no existe el dato

#remover elementos
my_other_set.remove("Victor")
print(my_other_set) # --> {'fenixlogan1', 42, 'hernandez'}

# limpia el set
my_other_set.clear()
print(len(my_other_set)) # --> 0, limpia la lista, elimina los elementos.


# Eliminar el set
del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {'Victor','Hernandez',45, 'fenixlogan1@gmail.com'}
my_list = list(my_set)
print(my_list) # --> ['fenixlogan1@gmail.com', 'Victor', 45, 'Hernandez']
# Es arriesgado hacer la transformacion de un set a una lista, por ejemplo
print(my_list[0])

my_other_set = {'Javascript',"PHP","Python"}
#union de sets
my_new_set = my_set.union(my_other_set)
print(my_new_set) #--> {'Javascript', 'PHP', 'fenixlogan1@gmail.com', 'Victor', 'Python', 45, 'Hernandez'}




