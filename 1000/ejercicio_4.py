# Solicitar el valor del radio de un circulo para calcular el area.
from math import pi
#Area = pi x radio al cuadrado

r = float(input("ingresar el radio del circulo: "))
area = round((pi * r **2),2)
print(f'El area de un circulo con radio {r} = {area}')
