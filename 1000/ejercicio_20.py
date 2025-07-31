# Emular el funcionamiento del producto de cadenas de caracteres

def producto_cadena(cadena, repeticion):
    """
    Emula el funcionamiento de un producto(*) de cadenas..
    """
    resultado = " "
    for i in range(repeticion):
        resultado = resultado + cadena

    return resultado


print('Python'*3)
print(producto_cadena('Python',3))