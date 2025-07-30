# Solicitar al usuario un numero n y calcular n + nn + nnn
# n = 3 + 33 + 333 = 369

n  = input ('escriba el valor de n: ')
nn = int('{}{}'.format(n, n))
# nnn = int('{}{}{}'.format(n, n, n))

nnn = int('%s%s%s' % (n,n,n))
n = int(n)

suma = n + nn + nnn
print(suma)
print(n)
print(nn)
print(nnn)