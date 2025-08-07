"""
Funciones Recursivas.
"""
#Es una funcion que se llama a si misma durante su ejecucion.

# Ejemplo: contar hasta cero

def contar_hasta_cero(n):
    if n <= 0:
        print("He terminado")
    else:
        print(n)
        contar_hasta_cero(n-1)
        
contar_hasta_cero(5)

print("-"*50)

def contar_hacer_cero_1(n):
    while n > 0:
        print (n)
        n -= 1
    print("he terminado")
    
contar_hacer_cero_1(5)

print("-"*50)


def reloj_back(n):
    while n > 0: 
        """
        tener en cuenta que el mientras, sea positivo, mientras el n sea mayor que cero, ejecuta la impresion y cada que pasa por el ciclo se reduce 1
        """
        print(n)
        n -=1
    print("fin de ciclo")


reloj_back(4)