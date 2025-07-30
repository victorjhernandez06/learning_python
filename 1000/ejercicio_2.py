# Exponer el uso basico de la funcion print

print("mostrar el texto en pantalla")

print("Ejemplo 2",end=' ') # Quitamos el salto de linea por defecto y anexamos solo un espacio en blanco
print("Ejemplo 2",end=' ') # Ejemplo 2 Ejemplo 2

print()
print('Python', 'es', 'tremendo') #--> Python es tremendo
print('Python', 'es', 'tremendo', sep='-') # cambiamos el separador por una linea # -- > Python-es-tremendo.

print()
print('{} es {}'.format('Python', 'tremendo!')) #--> Python es tremendo!

print()
numeros = [2, 3, 5, 7, 11]
print(numeros) # --> [2, 3, 5, 7, 11]
print(type(numeros)) # --> <class 'list'>

capitales = {'colombia':'bogota', 'peru':'lima'}
print(capitales) #--> {'colombia': 'bogota', 'peru': 'lima'}
print(type(capitales)) #-->  <class 'dict'>
