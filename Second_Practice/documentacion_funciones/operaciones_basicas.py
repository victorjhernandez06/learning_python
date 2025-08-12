def operaciones_basicas(a,b):
    """
    Realiza operaciones basicas entre numeros
    :param a:(int o float) Primer numero
    :param b:(int o float) Segundo numero
    :return: retorna una tupla con los resultados de las operaciones.
            -suma(int o float): suma de a y b.
            -resta (int o float): diferencia de a y b.
            -multiplicacion(int o float): producto de a y b.
            -division(float): cociente de a dividido por b (si b no es cero)            
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division


resultados = operaciones_basicas(8,4)
print(resultados)



