
def modificar_valor(x):
    x = x + 10
    print(f'dentro de la funcion: {x}') 
    

    
numero = 5
modificar_valor(numero) # --> 15
print('fuera de la funcion:', numero) # --> 5
