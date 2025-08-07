def factorial(n):
    """
    calcula el factorial de un numero entero no negativo
    
    :param n: (int) Numero entero no negativo.
    :return (int) Retorna el factorial de n.
    :raises RecursionError: Si n es un numero negativo
    """    
    
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n -1)
    
    
resultado_factorial = factorial(4)
print(resultado_factorial)