"""
Para cambiar el valor de una variable global dentro de una funcion.. 
le debemos colocar la palabra global.
"""

y = 20

def function():
    global y
    y = 30
    print(y, "impresion dentro la funcion")
    

function() # 30 impresion dentro la funcion
print(y, 'immpresion fuera de la variable') # 30 immpresion fuera de la variable




