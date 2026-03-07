# Ejercicio 59: Calcular la estatura (dada en pies y pulgadas)en centimetros

#En un pie hay 30.48 cms, en una pulgada hay 2.54 cm

print("escriba su estatura (ft y pulgada")

pies = float(input('Pies: '))
pulgadas = float(input('Pulgadas: '))

cm = pies * 30.48
cm+= pulgadas * 2.54

print('Su estatura es {} cm'.format(cm))

#comprobacion

feet = cm * 0.0328084
print('Su estatura es {} feet'.format(feet))
