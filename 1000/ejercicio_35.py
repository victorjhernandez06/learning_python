# Crear una funcion unicamente para sumar numeros enteros

def sumar(x,y):
    try:
        x = int(x)
        y = int(y)
        return x+y
    except ValueError:
        raise TypeError('El valor debe ser un entero o canvertible a entero')

print(sumar(2,3))
print(sumar(23,23))
print(sumar(23,'2'))
print(sumar('a','r'))