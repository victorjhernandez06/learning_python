# Validar dos numeros. Si son iguales o la suma o el valor absoluto son 5:

def validar_numeros(x,y):
    """
    Evalua dos numeros
    """
    if x == y or (x + y )== 5 or abs(x -y)==5:
        return True
    else:
        return False

print(validar_numeros(3,3))
print(validar_numeros(5,7))
print(validar_numeros(16,11))
print(validar_numeros(4,1))
