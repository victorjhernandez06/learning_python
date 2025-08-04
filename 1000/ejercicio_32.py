# Calcular la suma de tres numeros si todos son diferentes, en caso contrario la suma sera cero (0)

def sumar(x,y,z):
    """ Suma tres numeros. si al menos dos numeros son iguales, la suma sera cero 0"""
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z

print(sumar(2,3,4))
print(sumar(2,2,4))