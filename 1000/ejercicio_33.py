# Sumar dos numeros. Si la suma esta entre 10 y 30 retornar 30.
def sumar(x,y):
    suma = x + y

    if suma in range(10,30+1):
        return 30
    else:
        return suma

print(sumar(2,3)) #--> 5
print(sumar(10, 11)) #--> 30
print(sumar(7,3)) #--> 30
print(sumar(23,23)) #--> 46