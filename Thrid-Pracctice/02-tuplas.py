# Creating a list from one tuple
# the tuple have (), the list have [].
"""
Propiedades de las tuplas
Tuples properties
1.- Son listas inmutables
2.- Permiten extraer porciones pero el resultado es una nueva tupla
3.- No permite busquedas (no index)4.- Permiten comprobar si un elemento se encuentra dentro de una lista.
4.- La mejor caracteristica es su orden.

1.- They are inmutable lists
2.- They allow you to extract portions but the result is a new tuple
3.- Allow you to check if an elements is within a list.
4.- The main characteristics or tuples are being ordered.
"""

# Creating an empty tuple
tup = ()
print(tup)
#-> ()

#using String
tup = ('Geeks','For')
print(tup)
#('Geeks','For')

#Using List
li = [1, 2, 3, 4, 5, 6]
print(tuple(li))
#(1, 2, 3, 4, 5, 6)

#using Built-in Function.
tup = tuple('Geeks')
print(tup)
#('G','e','e','k','s')

"""
Creating a tuple with mixed detatypes
"""
#creating a tuple with a mixed Datatypes.
tup =  (2, 'Welcome', 7, 'Geeks')
print(tup)
# -> [2, 'Welcome', 7, 'Geeks']

#Creating a tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('pyhton', 'geek')
tup3 = (tup1, tup2)
print (tup3)

#creating a tuple with repetition
tup1 = ('Geeks')*3
print(tup1)

#creating a tuple with thw use a top
tup = ("Geeks")
n =5
for i in range (int(n)):
    tup = (tup,)
    print(tup)

#comprobar si hay elementos dentro de la tupla

#accesing of tuples
tup = tuple ('Geeks')
print(tup[0])
# -> G

#accesing a range of elements using slicing
print(tup[1:4])
print(tup[:3])
tup = ("geeks",'For','Geeks')

#this line unpack values of tupel
a, b, c = tup
print(a)
print(b)
print(c)

#geeks
#For
#Geeks

object_tuple = ("victor", 42, 1983)
name, age, year = object_tuple
print("--unpack values--")
print(name)
print(age)
print(year)
print("--unpack values--")
"""
Concatenation of Tuples
"""
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)
#(0,1,2,3, 'Geeks', 'For', 'Geeks')

"""
Slicing of tuple
Separacion de tuplas
"""
#silicing of a tuple with numbers
tup = tuple("GEEKFORGEEKS")

#removing first element
print(tup[1:])
#('E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S')

#reversing the tuple
print(tup[::-1])
#('S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G')

#Printing elements of a range
print(tup[4:9])
#('S', 'F', 'O', 'R', 'G')

"""
Deleting a Tuple
"""
tup = (0, 1, 2, 3, 4)
del tup
# print (tup)
#ERROR
#Traceback (most recent call last):
    #file<'main.py'>, line 130.. in <module>
#NameError: name 'tup' is not defined

#Conver list in tuple
mitupla = ( "juan", 12, 1, 19.3)
milista  = list(mitupla)
print(milista)
#answers-> ['juan', 12, 1, 19.3]

#convert a list in a tuple
mituple = tuple(milista)
print (mituple)
#-> ('juan', 12, 1, 19.3)

#metodo count
#permite contar cuantos elementos estan dentro de una tupla
print(mituple.count(12))
# el resultado es 1

#Metodo Len,
#Nos permite averiguar la longitud de una tupla.
#solo te dice cuantos elementos tienes en la tupla.
print(len(mituple))

# tupla unitaria
mitupla1 = ("victor")
print(len(mitupla1))
# 1

#podemos escribir la tupla sin los parentesis, ojo con esto
mitupla2 = "victor", 42, "pythonMaster"
print(mitupla2)

