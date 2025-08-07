def modificar_lista(lista):
    lista.append(4)
    print('dentro de la funcion',lista)
    
"""
Cuando entro a la funcion entro y se agrego el numero 4, aqui en paso por referencia, si se modifican, al contrario del paso por valor, donde no se afecta el objeto original, en el paso por referencia a objeto, si modifica al objetoo que pasamos.
"""

mi_lista = [ 1, 2, 3]
modificar_lista(mi_lista)
print('Fuera de la funcion', mi_lista)