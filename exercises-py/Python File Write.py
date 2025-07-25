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

# encriptar("prueba de texto")
# print("")
# desencriptar('pxrxuxexbxax xdxex xtxexxxtxox')

def encriptarArchivo(rutaArchivo):
    file = open(rutaArchivo,'r')
    texto = file.read()
    file.close()
    textoEncriptado = encriptar(texto)

    file = open(rutaArchivo,'w') # w permite reemplazar todo.
    file.write(textoEncriptado)
    file.close()
    print("Archivo encriptado")

def desencriptarArchivo(rutaArchivo ):
    file = open(rutaArchivo,'r')
    texto = file.read()
    file.close()
    textoDesencriptado = desencriptar(texto)

    file = open(rutaArchivo,'w') # w permite reemplazar todo.
    file.write(textoDesencriptado)
    file.close()
    print("Archivo Desencriptado")

# encriptarArchivo()
# desencriptarArchivo()

respuestaEoD = input("presion 'E' para encriptar o 'D' para desencriptar: ")
rutaArchivo = input('Ingrese la ruta del archivo: ')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
elif respuestaEoD == 'D':
    desencriptarArchivo(rutaArchivo)
else:
    print('Elige una de las dos opciones, E=Encriptar, D=Desencriptar')

