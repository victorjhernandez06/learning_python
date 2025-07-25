"""Python File Write"""
#
# file = open('text.txt','a')
# file.write('Test save on directories')
# file.close()

# file = open('text.txt','r')
# print(file.read())

# Encriptador
def encriptar(texto):
    # print('Funcion para Encriptar '+ texto)
    textofinal =""
    for letra in texto:
        textofinal += letra + 'x'
    return textofinal


def desencriptar(texto):
    # print('Funcion Desencriptar '+ texto)
    textofinal = ""
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textofinal += letra
        contador += 1
    return textofinal

file = open('text.txt','a')
file.write('Test save on directories')
file.close()