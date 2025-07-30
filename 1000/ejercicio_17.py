# Crea una funcion para determinar si  un numero es carcano a 1000 o a 2000

def cercania(n):
# Comprueba si un numero dado es cercano a 1mil o a 2mil.
    return (abs(1000-n)<100) or (abs(2000-n)<100)
