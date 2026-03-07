#Ejercicio 56: Obtener el tamaño de la ventana de la terminal.
# Determinar cuantas filas y columnas tiene la ventana.
import fcntl, termios, struct

def calcular_terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0,termios.TIOCGWINSZ,struct.pack('HHHH',0,0,0,0)))
    return th, tw

print(calcular_terminal_size())
