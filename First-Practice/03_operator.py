## Operadores aritmeticos -> suma +, resta-, multiplicacion *
## Operadores de comparacion
## operadores de asignacion
## operadores Logicos
## Operadores de membresia
## operadores de identidad

##Aritmeticos
##Suma
compra1 = float(25.5)
compra2 = 12.75
total = compra1 + compra2
print ("la nota tota es de:",total)


##Promedio
nota1 = 10
nota2 = 45
nota3 = 90
promedio = (nota2+nota1+nota3)/3
print("El promedio es de ", promedio)

##Operadores de comparacion
numero = 7
if numero % 2 == 0:
    print("el numero es par")
else:
    print ("El numero es impar")

nota_estudiante = 3
nota_minima =  3.00
if nota_estudiante >= nota_minima:
    print("El estudiante ha aprobado")
else:
    print("El estudiante ha reprobado")


##Operadores de asignación // Assignment operator`s
##Asignacion Simple // simple assignment
"""
name = input("write your name: ")
print("Hi, nice to meet too:", name)
"""


#Operadores Logicos  // Logical Operators
#if else elif

dinero_base = 22
credito_disponible = 13

if dinero_base >= 20 and credito_disponible >= 14:
    print("credito aprobado")
else:
    print("Necesitas mas dinero")

if dinero_base >= 20 or credito_disponible >= 14:
    print("Puedes abrir tu cuenta de ahorro")
elif dinero_base >=24 or credito_disponible >= 13:
    print ("Puedes hacerlo mejor")
else:
    print("Ahorra mas!!")

hora = 14
if hora <12:
    print("buenos dias")
elif hora <18:
    print("Buenas tardes")
else:
    print("buenas Noches")

##WHILE
## permite ejecutar una parte del codigo mientras la condicion se cumpla
## Cuando la condicion se cumpla, lo que esta dentro del while no se ejecuta

contador = 0
while contador < 5:
    print("el contador es:", contador)
    contador += 1
    #contador = contador + 1

##rjemplo for
##
frutas = ["manzana", "uvas","melocotones","pera","peritas"]
print (frutas[1])
for fruta in frutas:
    print(fruta)

