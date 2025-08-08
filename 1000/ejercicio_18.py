# Calcular la suma de tres numeros, e incluir una condicion de igualdad

def sumar_numeros(a,b,c):
    """
    calcula la suma de los tres numeros, si los tres numeros son iguales, la suma se multiplica por 3.
    """
    suma = a + b + c
    if a == b and a == c:
        suma *=3

    return suma

print(sumar_numeros(35,35,35))
print(sumar_numeros(2,1,2))
print('-'*50)
a = int(input('introduzca a:'))
b = int(input('introduzca b:'))
c = int(input('introduzca c:'))
print(sumar_numeros(a,b,c))