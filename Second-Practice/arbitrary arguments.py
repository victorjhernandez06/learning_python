"""
Argumentos Arbitrarios
Arbitrary Arguments
"""

def sum_numeros(*numeros):
    print(numeros) #--> (1, 2, 3, 4, 5, 6)
    print(type(numeros)) # --> <class 'tuple'>
    resultados = sum(numeros) #--> 21
    print(resultados)
    
    
sum_numeros(1,2,3,4,5,6)
# *args --> al colocar todos los argumentos, se empaquetan en una tupla.



