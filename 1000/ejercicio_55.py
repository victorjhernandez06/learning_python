#Ejercicio 55: Convertir un numero binario en entero.


cadena = '1001'

entero = int(cadena, base=2)
print(entero)
print(type(entero))

#validacion
#conversion 1001 = 1*10^3 + 0*10^2 + 0*10^1 + 1*10^0
# --> 8 + 0 + 0 + 1  --> resultado = 9

