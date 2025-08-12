def cuadrado(x):
    return x*x

def cubo(x):
    return x ** 3


def aplicar_funcion_a_lista(funcion, lista):
    #creo una lista vacia, para que los valores se creen y se integren a esta usando el append method.
    resultado = []
    #itero con un bucle for, la lista que tenemos.
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado

lista_numeros = [1, 2, 3, 4, 5]

resultado = aplicar_funcion_a_lista(cuadrado, lista_numeros)

print(resultado) # -->[1, 4, 9, 16, 25]


resultado1 = aplicar_funcion_a_lista(cubo, lista_numeros)
print(resultado1)