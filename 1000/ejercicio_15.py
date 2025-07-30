# Calcular el volumen de una esfera a partir del radio dado.
from math import pi

r = int(input("indica el radio de la esfera: "))

r_al_cubo = r ** 3
volumen = (4/3)*pi*r_al_cubo

print(volumen)
print(f'El volumen de la esfera es: {volumen} unidades cubicas')






#wolframAlpha, motor de conocimiento que podemos consultar