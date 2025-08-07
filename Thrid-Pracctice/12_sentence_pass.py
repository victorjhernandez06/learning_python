# Programa principal
from math import factorial

# Definicion de funciones:
def factorial(num):
    # pass #--> cuando la funcion queda pendiente
    # #pendiente
    fact = 1
    for i in range(num):
        pass # Pendiente falta algo aqui.    
    return fact

# Script para encontrar el factorial
# Programa Principal.
numero  = int(input("Ingrese un numero natural: "))
if numero >= 0:
    el_factorial = factorial(numero)
    print(f"el factorial de: {numero} es {el_factorial}")
else: 
    print("no existe el factorial de un numero negativo.")