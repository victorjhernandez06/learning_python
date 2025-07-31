# Crear un histograma a partir de una lista de enteros.

# Analisis:
# [2,1,5,3] = es una frecuencia para cada uno de los elementos
# **
# *
# *****
# ***

def crear_histograma(lista, caracter='*'):
    for e in lista:
        for i in range(e):
            print(caracter, end="")
        print()

lista = [2,1,5,3]
crear_histograma(lista)
# **
# *
# *****
# ***

print()

lista2=[2,7,13,19,11,2,3,4,5,6,7]
crear_histograma(lista2)
# **
# *******
# *************
# *******************
# ***********
# **
# ***
# ****
# *****
# ******
# *******