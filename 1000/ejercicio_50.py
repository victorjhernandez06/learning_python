# Modificaar el comprotamiento de la impresion de la funcion print

print('Python es tremendo', end='')
print()

for i in range(10):
    print("*", end='')  # Colocar end, al final de la instruccion print, nos permite evitar el salto de linea que viene por defecto

print()

print('Python','es','tremendo', sep='-')