# Calcular el minimo comun multiplo.

#MCM: es el numero positivo mas peque#o qe es multiplo de dos numeros.

def mcm(x , y):
    z  = max(x , y)

    while True:
        if (z % x == 0) and (z % y == 0):
            return z

        z += 1

print(mcm(2,4))  #--> 4
print(mcm(32,13)) # --> 416
print(mcm(17, 15)) # --> 255

