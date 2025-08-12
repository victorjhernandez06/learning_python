#Funciones --functions
#Las funciones don bloques de código reutilizable, utilizamos la palabra def
#functions are reusable code blocks.

def nombre_function():
    print("victor Hernandez")

nombre_function()

#estado =1 -> encendido =0 -> apagado
def encender(estado):
    if estado == 1:
        print("El auto esta encendido")
    else:
        print("Auto Apagado")
encender(0)


def apagar(estado):
    if estado == 1:
        print("Apagando auto ... auto apagado")
    else:
        print("Auto Apagado!! ")
apagar(1)

def avanzar(estado):
    if estado == 1:
        print("Auto en marcha")
    else:
        print("El auto esta apagado.")
avanzar(1)

def frenar():
    print("Usted esta usando el freno")
frenar()

def control(estado):
    if estado == 1:
        apagar(1)
    else:
        encender(1)

control(1)
