# Crear una cadena de caracteres multilineas

# Podriamos ir a view --> active editor --> soft-wrap
cadena = "Esto es un texto largo que queremos cortar con ptyhon y ver como se puede adaptar a un espacio muy reducido de tu pantalla, es decir ser representado en una sola linea, haciendo visible todo el texto en el espacio que hay en la pantalla"

# Podriamos concatenar lineas con +=, cerramos con " y empezamos la nueva linea con +=
cadena1 = "Esto es un texto largo que queremos cortar con ptyhon y ver como se puede adaptar"
cadena1 += "a un espacio muy reducido de tu pantalla, es decir ser representado en una sola linea, "
cadena1 += " haciendo visible todo el texto en el espacio que hay en la pantalla"


# podriamos utilizar las comillas triples """  xx  """ y con ello solo vamos a dar enter para saltos de linea.

cadena2 = """Esto es un texto largo que queremos cortar con 
ptyhon y ver como se puede adaptar a un espacio muy reducido 
de tu pantalla, es decir ser representado en una sola linea, 
haciendo visible todo el texto en el espacio que hay en la pantalla"""


print(cadena)
print('-'*50)
print(cadena1)
print('-'*50)
print(cadena2)
