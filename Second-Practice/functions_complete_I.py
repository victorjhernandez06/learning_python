### FUNCIONES EN PYTHON ###
### FUNCTIONS IN PYTHON ###


"""
Valores por defecto en una funcion.
Default values in a function.
"""

def exponente(base, exp=2):
    resultado = base ** exp
    print(resultado)
    
    

# Llamadas a la funcion sin expecificar el exponente.
# Calls a function without specifying the exponent.
exponente(3)

# Llamadas a un funcion especificando el exponente.
# Calls a function specifying the exponent.
exponente(3,4)


