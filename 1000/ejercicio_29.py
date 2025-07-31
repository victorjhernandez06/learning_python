# Calcular el area de un triangulo.

#formula para el calculo del area base x altura entre 2
base = None
altura = None

# validacion de datos
while True:
    try:
        base = float(input('Ingrese la base del triangulo: '))
        break
    except:
        print('El formato del dato debe ser numerico')

while True:
    try:
        altura = float(input('Ingrese la altura del triangulo: '))
        break
    except:
        print('El formato del dato debe ser numerico')

# calculo del area.
area = (base * altura)/2
print(f'El area del triangulo es: {area}')
print(type(area))