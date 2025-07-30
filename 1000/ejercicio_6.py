# Obtener un conjunto de numeros separados por coma y crear una lista.

# 2, 8, 9, 1, 4

#solicitud de datos
entrada = input('escriba varios numeros separados por coma: ')
numeros = entrada.split(',') # Usamos este metodo, y recordemos que no son numeros, son cadenas de caracteres.

print(numeros) # --> ['1', '2', '3', '4', '5', '6', '11']
print(type(numeros)) # --> <class 'list'>

