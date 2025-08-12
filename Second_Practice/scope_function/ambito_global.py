y = 10  #variable global

def function():
    print(y, ' Impresion de variable dentro de la funcion')
    
    
function() #imprime la variable que se encuentra dentro de la funcion, pero el valor lo toma de la variable global.

print(y) # imprime la variable global que esta fuera de la funcion.



"""
Modificando la variable global dentro de la funcion
"""

z = 10
def funcion_1():
    z = 20
    print(z, 'variable dentro de funcion') 


funcion_1() # Imprime la variable local, que se encuentra dentro de la funcion
print(z, "variable global") # Imprime la variable global, que se encuentra fuera de la funcion.