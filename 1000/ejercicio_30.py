# Calcular el maximo comun divisor de un numero.

#MCD: Es el numero mas grande que divide dos numeros.

def mcd(x,y):
    mcd = 1 #usamos el numero 1, porque es el mcd de cualquier numero.

    if x % y == 0:
        return y

    for k in range(int(y/2),0, -1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
    return mcd

print(mcd (8,4))

print(mcd(13, 7))

