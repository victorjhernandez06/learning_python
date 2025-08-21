# Crear una tupla nombrada para representar un punto en plano.
from collections import namedtuple
from math import sqrt

# class Punto:
#     def __init__(self, x, y):
#         self.x = x #campo de instancia
#         self.y = y #campo de instancia.


Punto = namedtuple('Punto',['x','y'])
punto_1 = Punto(2,3)
punto_2 = Punto(-3,-5)

print(punto_2)
print(punto_1)

#crear una funcion que calcule la distancia entre los dos puntos.

def calcular_distancia(punto_1 , punto_2):
    return sqrt((punto_1.x - punto_2.x)**2 + (punto_1.y - punto_2.y)**2)

print(calcular_distancia(punto_1,punto_2))

