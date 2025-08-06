# args and kwargas
# al final obtenemos un diccionario..


def funcion_combinada(*args, **kwargs):
    print('Argumentos posicionales:', args)
    print('Argumentos de palabra clave:', kwargs)
    
    
    
funcion_combinada(1,2,3, nombre='victor',edad=43)
    