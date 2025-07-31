# Calcular la diferencia de conjuntos con colores:

colores_lista_1 = ['Negro','rojo','verde','Blanco']
colores_lista_2 = ['Blanco','Azul','Verde','Gris','Amarillo','Verde']

# conjunto A, B; diferencia --> A-B; A / B, es encontrar aquellos elementos que tiene A y que no tiene B.

colores_conjunto_1 = set(colores_lista_1)
colores_conjunto_2 = set(colores_lista_2)

#los objetos Set, cuentan con un conjunto que puede calcular la diferencia

diferencia = colores_conjunto_1.difference(colores_conjunto_2)
print(diferencia) #--> {'Negro', 'verde', 'rojo'}
print(type(diferencia))  #--> <class 'set'>



