# Encriptador
def encriptar(texto):
    textofinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textofinal += chr(ascii)
    return textofinal


def desencriptar(texto):
    textofinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textofinal += chr(ascii)
    return textofinal


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
    print('Elige una de las dos opciones, E=Encriptar, D=Desencriptar: ')

