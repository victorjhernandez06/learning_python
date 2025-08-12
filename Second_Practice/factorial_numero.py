## --> Funciones Recursivas: Factorial de un numero

# 5! = Calcular el producto desde 1 hasta el indicado.. 1*2*3*4*5 ==> 5!, la exclamacion en este caso indica factorial.


def factorial_numero(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_numero(n - 1)
    

print(factorial_numero(5))

resultado = factorial_numero(5)
print(resultado)