# Potencia_valor

#funciones que pueden tomar 1 o mas argumentos y devolver funciones

def cuadrado(x):
    return x*x

def cubo(x):
    return x ** 3


#definimos la funcion

def aplicar(funcion, valor):
    return funcion(valor)


resultado = aplicar(cuadrado, 5)
print(resultado)

resultado1 = aplicar(cubo, 2)
print(resultado1)