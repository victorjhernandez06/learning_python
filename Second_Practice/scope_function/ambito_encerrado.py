"""
Un ambito encerrado ocurre cuando tenemos una funcion interior dentro de una funcion, a esto se le llama funcion anidada.
"""

def exterior():
    a = 50 #variable local del ambito exterior
    
    def interior():
        print(a) # la funcion anidada puede acceder a la variable que tiene en el exterior.
        
        
    interior() # --> 50
    

exterior() # --> muestra el valor de la llamada print de la funcion anidada.
