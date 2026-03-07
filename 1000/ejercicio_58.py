# Ejercicio 58: Calcular la suma de los primeros n numeros enteros

# Usando la formula de Gauss: n * (n+1)/2

n = 10

suma = n * (n + 1) / 2
print(suma)
print()

#Usando un ciclo:
suma = 0
for i in range(1,n + 1):
    suma = suma + i
print(suma)
print()

# Usando la funcion sum

suma = sum(range(1,n+1))
print(suma)
print()
