# Imprimir en la salida estandar de errores.
import  sys
#modulo incorporado en Python.

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint('Este es un mensaje de error')
##print('Esto es un error', file = sys.stderr)
