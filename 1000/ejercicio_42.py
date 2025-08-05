# Encontrar la arquitectura computacional del shell
# Debemos ver donde corremos el shell. si es de 32 o 64 bits.

import struct
#dentro de struct tenemos la funcion callsite, y nos calcula la cantidad de bites en un puntero..

print(struct.calcsize('P'))
# si nos da 8 bit, quiere decir que la estructura es de 64.
# si nos da 4 bit, quiere decir que la estructura es de 32

#Esto lo comprobamos multiplicando el resultado por 8
# 8 x 8 ==> 64bit ==> System 64
# 4 x 8 ==> 32bit ==> System 32