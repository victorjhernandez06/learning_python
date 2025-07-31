# Crea una funcion para determinar si  un numero es carcano a 1000 o a 2000

def cercania(n):
    return (abs(1000-n)<100) or (abs(2000-n)<100)

print(cercania(1000))
print(cercania(950))
print(cercania(102))
print(cercania(4000))
