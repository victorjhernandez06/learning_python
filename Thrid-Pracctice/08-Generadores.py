"""
Generadores en pyhton
# Estructuras que extraen valores de una funcion y se almacenan en ojetos iterables, los puedes recorrer con bucles como for, while u otros.
# Los valores se almacenan de uno en uno.
# Permanecen en estado pausado dentro del generador.
# Entre llamada y llamada el generador entra en estado de suspension.
"""

def generaPares(limite):
    num = 1
    mi_lista = []

    while num < limite:
        mi_lista.append(num*2)
        num +=1

    return mi_lista

print(generaPares(10))

#Esto mismo utilizando un generador

def generaPares1(limite):
    num = 1

    while num < limite:
        yield num * 2
        num +=1

devuelvePares = generaPares1(10)
for i in devuelvePares:
    print(i)

devuelvePares1 = generaPares1(10)
print(next(devuelvePares1))
print("Aqui podria ir mas codigo")
print(next(devuelvePares1))
print("Aqui podria ir mas codigo")
print(next(devuelvePares1))
print("Aqui podria ir mas codigo")
print(next(devuelvePares1))
print("Aqui podria ir mas codigo")
print(next(devuelvePares1))
print("Aqui podria ir mas codigo")
print(next(devuelvePares1))
print("Aqui podria ir mas codigo")
print(next(devuelvePares1))