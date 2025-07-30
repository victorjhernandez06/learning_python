# Crea una funcion para evaluar un numero y realizar una operacion.

#fn(n): si n <= 15 +> 15 - n; (15-n)*2

def diferencia(n):
    """
    Calcula la diferencia del valor pasado como argumento.
    se deben seguir dos reglas.
    :param n:
    :return:
    """
    if n <= 15:
        return 15-n
    else:
        return (15-n)*2

print(diferencia(17)) #--> -4
print(diferencia(3)) #--> 12