# contador = 0
# my_email = input("Introduce tu email: ")
#
# for i in my_email:
#     if (i == "@" or i=="."):
#         contador +=1
#
# if contador == 2:
#     print("Email es correcto")
# else:
#     print("email incorrecto")

# Range

for i in range(5):
    print(i)

# -> 0
# -> 1
# -> 2
# -> 3
# -> 4

"""
Bucle for
"""

# Notaciones especiales con print
# unir o concatenar valores de texto con variales


for i in range(5):
    print(f"Valor de la variable: {i}")

# Valor de la variable: 0
# Valor de la variable: 1
# Valor de la variable: 2
# Valor de la variable: 3
# Valor de la variable: 4

for i in range(5, 9):
    print(f"El valor de i: {i}")
# El valor de i: 5
# El valor de i: 6
# El valor de i: 7
# El valor de i: 8

for i in range(5, 20, 2):
    print(f"El valor de i: {i}")
# El valor de i: 5
# El valor de i: 7
# El valor de i: 9
# El valor de i: 11
# El valor de i: 13
# El valor de i: 15
# El valor de i: 17
# El valor de i: 19


"""
funcion len -> devuelve la longitud de un string, 
devuelve el numero de caracteres que tiene un string
"""
#
# valido = False
#
# # email = input("introduce tu email: ")
#
# for i in range (len(email)):
#     if email[i] == "@":
#         valido = True
#
# if valido:
#     print("El email es correcto")
# else:
#     print("Email incorrect")

"""Python While Loop Syntax:Python While Loop Syntax:"""

cnt = 0
while (cnt < 3):
    cnt +=1
    print("python")

"""For Loop in Python"""

n = 4
for i in range(0, n):
    print(i)

li = ['geeks', 'for', 'geeks']
for i in li:
    print(i)

tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)

s = "victor"
for i in s:
    print(i)

d = dict({'x':123, 'y':354})
for i in d:
    print("%s %d"%(i, d[i]))

set1 = {1,2,3,4,5,6}
for i in set1:
    print(i)

"""Iterating by the Index of Sequences"""
list = ['geeks', 'for', 'geeks']
for index in range (len(list)):
    print(list[index])

"""Using else Statement with for Loop in Python"""
list = ['geeks', 'for', 'geeks']
for index in range(len(list)):
    print(list[index])
else:
    print("Inside else block")


"""Loop Control Statements"""
for letter in 'VictorHernandez':
    if letter =='e' or letter == 'z':
        continue
    print('Current letter:', letter)

"""Break Statement"""
for letter in 'KarinaJimenez':
    if letter == 'e' or letter == 'z':
        break
    print('Current letter : ', letter)

"""Pass Statement"""
for letter in 'AdrianHernandez':
    pass
print('last letter :', letter)

"""How for loop works internally in Python?"""
fruits = ['apple','orange', 'kiwi']
for fruit in fruits:
    print (fruit)

fruits = ['apple','orange', 'kiwi']
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break


