import math
"""
If Conditional Statement in Python
"""
from operator import truediv

"""
Conditional Check with if Statement
"""
#if statement example
if 10 > 5:
    print("10 greater than 5")

print("program ended")
# -> 10 greater than 5
# -> program ended"

# if.. else statement example
x =  3
if x == 4:
    print("Yes")
else:
    print("No")
# -> No

# -> Ejemplo 2: Cadena if..else anidada para múltiples condiciones
# -> Nested if..else Chain for multiple conditions.

# if..else chain statement
letter =  "A"
if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't A, B and C")

# -> Letter is A.

"""
Nested if Statement
Declaracion if Anidado
"""
# Si la condicion primaria no se cumple, se necesitaria revisar la condicion secundaria.

"""
if(condition1):
    # Executes when condition1 is true
if (condition2):
    # Executes when condition2 is true.
"""

# Nested if statement example
a = 10

if a > 5:
    print ("Bigger than 5")

    if a <= 15:
        print("Between 5 and 15")

# -> Bigger than 5
# -> Between 5 and 15

"""
if-elif Statement in Python
"""

#if - elif statement sxample
letter = "A"

if letter == "B":
    print("letter is B")
elif letter == "C":
    print("letter is C")
elif letter == "A":
    print ("letter is A")
else:
    print("letter isn't A, B or C")
# -> letter is A

# Can We Use Elif in Nested If?
# yes.

x = 10
y = 5
if x > 5:
    if y > 5:
        print("X is greater than 5")
    elif y == 5:
        print("x is greater than 5 and y is 5")
    else:
        print("x is greater than 5 and y is less than 5")
# -> x is greater than 5 and y is 5


"""
Nested-if statement in Python
"""
age = 30
member = True

if age > 18:
    if member:
        print("Ticket price is $12.")
    else:
        print("Ticket price is $20.")
else:
    if member:
        print("Ticket price is $8.")
    else:
        print("Ticket price is #10.")

# -> Ticket price is $12.


"""
Nested if with else Condition
"""
i = 0
# if Condition 1
if i != 0:
    # Condition 1
    if i > 0:
        print("Positive")

    # Condition 2
    if i < 0:
        print("Negative")
else:
    print("Zero")
# -> Zero

"""
Nuevo Conditional WHILE
"""
i = 1

while i <= 10:
    print("Ejecucion " + str(i))
    i = i + 1

print("Termino la ejecucion del programa.")

"""
WHILE CON LA EDAD
"""
# edad = int(input("Introduce tu edad por favor: "))
edad = 12
while edad < 0:
    print("Edad incorrecta, intenta de nuevo")
    edad = int(input("Introduce tu edad por favor: "))

print("Gracias lo hiciste excelente")
print("La edad del aspirante es:" + str(edad))

"""
Edad del estudiante
"""

print("Programa de calculo de raiz cuadrada")
# numero=(int(input("Introduce un valor numerico: ")))
numero=25
intentos = 0

while numero<0:
    print("No exite raiz de numero negativo")

    if intentos == 2:
        print("Demasiados intentos, programa finalizado")

    numero=(int(input("Introduce un valor numerico: ")))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + " es: " + str(solucion))


"""
Continue, pass y else.
"""

for letra in "Python":

    if letra == "h":
        continue

    print ('viendo la letra:' + letra)

# viendo la letra:P
# viendo la letra:y
# viendo la letra:t
# viendo la letra:o
# viendo la letra:n
# TODAS LAS LETRAS MENOS LA QUE INDIQUE EN EL IF, QUE DEJARA POR FUERA
# Y APLICARA EL CONINUE

nombre ="Victor Hernandez"
contador = 0
for i in nombre:
    if i==" ":
        continue
    contador +=1
print(contador)

"""
Instruccion Pass
Casos muy concretos, simplemente devuelve un nulo.
"""
#ctrl + C  --> Romple el bucle infinito,

class mi_clase:
    pass #implementar mas tarde

"""
Instruccion ELSE
"""

email = input("introduce tu email, por favor: ")
for i in email:
    if i == "@":
        arroba = True
        break;
else:
    arroba = False
print(f"El correo es valido: {arroba}")

# La instruccion else, en este caso se va a ejecutar es cuando el flujo
# del bucle termine de recorrer, no como en el if, que la lee si es falso,





