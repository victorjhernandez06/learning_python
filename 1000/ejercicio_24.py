# Simular el funcionamiento del operador in
# Nos permite comprobar dentro de una coleccion si el elemento esta dentro de ella.

print(5 in (2, 3, 5, 6, 7)) #--> True\\
print('k' in 'fork') #--> True
print('i'in 'fork') #==> False

def pertenece (lista, elemento):
    """
    Comprueba si un elemento esta en lista
    """
    for e in lista:
        if elemento ==  e:
            return True
    return False

print(pertenece([3,3,4,5,5],5))
print(pertenece('fork', 'k'))
print(pertenece('fork', 'i'))

print('-'*70)


print(pertenece(['F','o','r','k'], 'i'))
print(pertenece(['F','o','r','k'], 'k'))
