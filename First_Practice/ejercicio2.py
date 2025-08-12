from symtable import Function


class Animal:
    def comer(self):
        print("El Animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

##ADD NUMBERS
a = 12
b =15
#adding two numbers
res = a + b
print(res)

##USING INPUT
"""
a = input("first Number: ")
b = input("second Number: ")
#converting input to float and adding
rest = float(a) + float(b)

print (rest)
"""

##USING A FUNCTION
print("USING A FUNCTION")
def add(a, b):
    return a + b

#initializing numbers
a= 10
b= 20

#calling function
res = add (a,b)
print(res)


##USING LAMBDA FUNCTION
print("USING LAMBDA FUNCTION")
res1 =  lambda a, b: a + b
print(res1(11,22))

##USING OPERATOR.ADD
print("USING OPERATOR.ADD")
import operator
print(operator.add(10,3))

##USING SUM()
print("USING SUM()")
print(sum([2,3]))


## Find Maximum of two numbers in Python
a =  7
b = 3
print(max(a,b))

##USING CONDITIONAL STATEMENTS
a =  10
b = 3
if a > b:
    print(a)
else:
    print(b)

#USING TERNARY OPERATOR
a = 4
b  = 2
res =  a if a>b else b
print (res)

