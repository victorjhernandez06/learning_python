def exterior():
    a = 50 #variable local del ambito exterior
    
    def interior():
        a = 20
        print(a, "variable anidada")
    
    interior()
    print(a, "variable local")


exterior()


"""
No podemos, en la variable anidada, aplicar el cambio usado con la variable global.
en cambio ahora tenemos que utilizar la palabra "nonlocal"
"""

def exterior():
    b = 50 #variable local del ambito exterior
    
    def interior():
        nonlocal b # Con la palabra nonlocal, podemos modificar la variable local, dentro de una funcion anidada.
        b = 20 # --> aqui le asignamos el valor de 20, a la variable local.
        print(b, "variable anidada") 
    
    interior()
    print(b, "variable local") #--> aqui imprimimos la variable local modificada en la funcion anidada.


exterior() 
"""
Imprimimos el valor de la variable b, modificada en la funcion anidada. 
# 20 variable anidada
# 20 variable local
"""