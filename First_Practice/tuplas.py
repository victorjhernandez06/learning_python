#TUPLAS
#son iguales a las listas // they are same as the lists
#No se pueden modificar  // Cannot be modified
#Se acceden a sus valores al igual que en las listas
# Their values are accessed in the same way as in the lists.
# Se pueden desempaquetar
# Can be unpacked

tupla = (1,2,3,4,5)
print (tupla)
print (tupla[2])

#desempaquetar una tupla
#unpack tuples
tupla_datos = ("juan", 25,"Python")
nombre, edad, lenguaje = tupla_datos
print(tupla_datos)
print(nombre)
print(edad)
print(lenguaje)

#combinaciones de tuplas // tuples combination
#puedo juntar dos tuplas en 1 sola. // I can join two tuples into one

tupla2 = (10, 20, 30)
tupla_combinada = tupla + tupla2 + tupla_datos
print(tupla_combinada)
print(len(tupla_combinada))

#iterar sobre elemento
for elemento in tupla_combinada:
    print(elemento)

print("juan" in tupla_combinada)

#Retornar multiples valores desde una tupla
## Returning multiple values from a tuple

def coordenadas():
    x = 10
    y = 20
    return x,y
resultado = coordenadas() #Esto queda como una tupla y por lo tanto es inmutable
#this remains as a tuple and is therefore inmutable
print(resultado)

x,y = resultado
print(x)
print(y)
