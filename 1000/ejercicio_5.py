# Obtener la representacion inversa de una cadena de caracteres.

#Python ==> nohtyP

cadena = 'Python'
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i],end='')

print()
print(cadena[::-1]) #al indicar el -1, recorremos la cadena desde el final al principio.

