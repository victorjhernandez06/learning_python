#### ListS #### 
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# Lists are changeable, which means that we can change, add or remove items after the list
# has been created.
# Since lists are indexed, lists can have items with the same value:

my_list = ["apple", "banana", "cherry", "water melon"]
print(my_list[2])  # Output: ["apple", "banana", "cherry"]


#agregar elementos al final de la lista .append
#add items to the end of the list
#APPEND
my_list.append("Coco")
print(my_list)

#INSERT
#agregar un elemento en la lista, al comienzo
#Add an item to  the list, the beginning of the list
my_list.insert(0,"Mandarina")
my_list.insert(1,"Guanabana")
print(my_list)

#Eliminar Elementos de una lista.
#Remove items from a list.
##remove
my_list.remove("Mandarina")
print(my_list)

elemento = my_list.pop(1)
print (elemento)
print(my_list)

##Ordenar una lista
##Sort the list
## SORT
lista_numero = [10,50,20,30]
lista_numero.sort()
print(lista_numero)

##podemos ordenar la lista de otra manera.
#REVERSE
lista_numero.reverse()
print(lista_numero)

#Longitud de las listas, colocamos dentro de la palabra reservada la lista.
##LEN
longitud = len(lista_numero)
print(longitud)
