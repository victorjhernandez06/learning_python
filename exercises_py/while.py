
contador = 0

while contador < 5:
    print("El valor de contador es: "+ str(contador))
    contador +=1
# El valor de contador es: 0
# El valor de contador es: 1
# El valor de contador es: 2
# El valor de contador es: 3
# El valor de contador es: 4

print() # Espacio vacio.
#Exercise 02
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print("El valor de contador es: "+ str(contador))

print() # Espacio vacio.

#Exercise 03
seguirChateando = True
while seguirChateando:
    texto  = input('>')
    if texto == 'exit':
        seguirChateando = False
    texto = texto.replace(':)','😁')
    texto = texto.replace(':(','☹')
    texto = texto.replace(':P','😜')
    texto = texto.replace(':*','😶')
    texto = texto.replace(':s','️😴')
    print(texto)


