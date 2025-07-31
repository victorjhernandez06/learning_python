# Generar un conjunto de numeros aleatorios y determinar cuales son impares.

# k mod 2 == 1
from random import randint

numeros_aleatorios = [randint(1, 100)for _ in range(50)]

print(numeros_aleatorios)
print("Primera forma")

numeros_impares = filter(lambda n: n % 2 ==1, numeros_aleatorios)
print(list(numeros_impares))

print("Segunda forma")
def encontrar_impares(lista):
    impares = []

    for n in lista:
        if n % 2 == 1:
            impares.append(n)
    return impares
print(encontrar_impares(numeros_aleatorios))
