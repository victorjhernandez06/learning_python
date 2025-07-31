# Emular el funcionamiento de la join paa concatenar una lista.

numeros = [2,3,4,5,6]
# El resultado deberia de la concatenacion deberia ser --> #23456


print(''.join([str(n) for n in numeros])) # --> 23456, aqui creamos una concatenacion entre los elementos de la lista
print("*"*50)

def concatenar_lista(lista):
    resultado = ''
    for n in lista:
        resultado += str(n)
    return resultado

print(concatenar_lista(numeros))
# --> 23456
