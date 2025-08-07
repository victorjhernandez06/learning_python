"""BUCLES / LOOPS / CICLOS"""
# LOOPS

"""PYTHON WHILE LOOPS"""
# WHILE LOOP
# El while es como un if infinito y por ello podemos colocarle un else.
my_condition = 0

while my_condition < 10:
    print(my_condition) # Lo que se ejecuta, despes de esto colocamos el incremento.
    my_condition += 4 # Aumento de la condicion, cada que sale del while
else: 
    print("Ya despues de este numero superamos la codicion del while")
print("--> Aqui estamos fuera del While y seguimos ejecutando el programa")

# the while loop
# with the while loop we can execute a set of statements as log as a condition is true

# Exercise
# print i as long as i is less than 6

i = 1
while i < 6:
    print(i)
    i += 1
# 1
# 2
# 3
# 4
# 5
print('continue with more exercise from while loops...')

# The while loop requires relevant variales to be ready, in this example we need to define an indexing variable, i, which we set to 1.

"""The break statement"""
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3: 
        break  # Esto detiene la ejecucion del while al llegar a cumplirse al condicion.
    i += 1
# 1
# 2
# 3
print('continue with more exercise from while loops...')


"""The continue Statement"""
i = 0 
while i < 6:
    i += 1
    if i == 3:
        continue  # Esto indica que al cumplirse la condicion, se salta el valor indicado en if, es decir, cuando i == 3, saltara y continua con la ejecucion sin incluir a este en el resultado final del while.
    print(i) 
# 1
# 2
# 4
# 5
# 6   
print('continue with more exercise from while loops...')


"""The else statement"""
# with the else statement, we can run a block of code once when the condition no longer is true

# example
# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i = i + 1
else:
    print("i is no longer less than 6")
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6
print('continue with more exercise from while loops...')



"""Python for loops"""
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string)
# this is less like for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With he for loop we can execute a set statements, once for each item in a list, tuple, set, etc. 

# Exercises
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)
# 35
# 24
# 62
# 52
# 30
# 30
# 17

my_tuple  = (35, 1.44, 'victor','Hernandez','Adrian')
for element in my_tuple:
    print(element)
# 35
# 1.44
# victor
# Hernandez
# Adrian

setup_2025 = ['Linux Debian','Linux Ubuntu',"Windows 11"]
for myself in setup_2025:
    print(myself)
# Linux Debian
# Linux Ubuntu
# Windows 11

my_set = {'Karina', 'Mathias',10}
for element in my_set:
    print(element)
# 10
# Karina
# Mathias

my_dict = {'Nombre': 'Sofia', 'Apellido':'Hernandez', 'Edad':9}
for element in my_dict:
    print(element)
else:
    print("el bucle for ha finalizado")
# Nombre
# Apellido
# Edad
# el bucle for ha finalizado

# Si queremos iterar los valores dentro de un diccionario, debemos ponerlo en una lista, puesto que al iterar con el for, en un principio solo obtendremos las keys. 
# list(my_dict.values())
my_dict = {'Nombre': 'Sofia', 'Apellido':'Hernandez', 'Edad':9}
for element in list(my_dict.values()): #
    print(element)
# Sofia
# Hernandez
# 9



print('////---////')    
# Example
# print each fruit in a fruit list
objects = ['set_1','set_2','set_3']
for x in objects:
    print(x)
# set_1
# set_2
# set_3

"""Looping through a string"""
# Even string are iterable objects, they contain a sequence of characters.
for x in "computer":
    print(x)
# c
# o
# m
# p
# u
# t
# e
# r

"""The break statement"""
# with the break statement we can stop the loop before it has looped through all the items
# Example: Exit the loop when x is: step2

objects = ['step_1','step_2','Step3']
for x in objects:
    print (x)
    if x == 'step_2':
        break
# step_1
# step_2

# Example: Exit the loop when x is "step_x", but this time the break comes before the print
objects = ['step_1','step_2', 'step_3','step_x','step_4', 'step_5']
for x in objects:
    if x == 'step_x':
        break
    print(x)
# step_1
# step_2
# step_3  


"""The continue statement"""
# with the continue statement we can stop the current iteration of the loop, and continue with the next.
# Example: Do not print 'set_x'.
objects = ['step_1','step_2', 'step_3','step_x','step_4', 'step_5']
for x in objects:
    if x == 'step_x':
        continue
    print(x)
# step_1
# step_2
# step_3
# step_4
# step_5

"""The range() function"""
# To loop through a set a code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0, by default, and increments by  (by defaults), and ends at a specified number.
# Example: usign the range() function:
for x in range(6):
    print(x)
# 0
# 1
# 2
# 3
# 4
# 5

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value adding a parameter: range(2,6), which means values from 2 to 6 (but no including 6)
for x in range(2, 30, 5):
    print(x)
# 2
# 7
# 12
# 17
# 22
# 27

"""Else in For Loop"""
# the else keywords in a for loop specifies a block of code to be executed when the loop finished.

# example: print all numbers from 0 to 5, and print a message when the loop has ended.

for x in range(6):
    print(x)
else:
    print('finally finished')

# 0
# 1
# 2
# 3
# 4
# 5
# finally finished
 
# Break the loop when x is 3, and see what happens with the else block.
# Aqui el bloque se detiene por el break cuando 3 == 3, entonces, el else no se ejecuta. 
for x in range(6):
    if x == 3: break
    print(x)
else:  
    print("finally finished1") 
# 0
# 1
# 2

"""Nested  lopps"""
# A nested loops is lopp inside a loop
# The "inner loop" will be executed one time for each iteration of the "outer loop"


"""the pass statement"""
# for the loops cannot be empty, but if you for some reason have a for loop with not content, put in the pass statement to avoid getting an error.

for x in [0,1,2]:
    pass #aqui no pasa nada, el bucle solo queda en el aire, esperando a que algun dia le des utilidad, como esta vacio, para no generar error le colocas la palabra reservada pass.




