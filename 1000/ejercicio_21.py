#Generar los n primeros numeros pares positivos..

#Un numero es par, si calculado el modulo % entre dos (2) es igual a cero.

def generar_dumeros_pares (n = 100):
    """
    Genera los n primeros numeros pares positivos.
    :param n:
    :return:
    """
    pares = []

    contador = 0
    numero  = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        numero +=1
    return pares

n  = int(input('escriba la cantidad de numeros pares positivos: '))
if n > 0:
    pares =  generar_dumeros_pares(n)
    print(pares)
    print(f'Cantidad de pares:', len(pares))
else:
    print('El numero debe ser positivo.')
