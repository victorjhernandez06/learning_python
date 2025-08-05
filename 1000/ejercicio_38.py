# Resolver la expresion algebraica (x+y)*(x+y).

def evaluar_expresion(x,y):
    """
    Resuelve la expresion algebraica
    """
    return x**2 + 2 * x * y + y ** 2

x = float (input('Escriba el valor de x: '))
y = float (input('Escriba el valor de y: '))

print(evaluar_expresion(x,y))