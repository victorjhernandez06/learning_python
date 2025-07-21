"""
Ternary Operator in Python
"""


"""
Basic Example of Ternary Operator
"""

n = 5
res = "Even" if n % 2 == 0 else "Odd"
print(res)
# -> Odd


"""
Ternary Operator in Nested If else
"""

n = -5
res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)
# -> Negative


"""
Ternary Operator using Tuple
"""
n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)
# -> Odd


"""
Ternary Operator using Dictionary
"""
a = 10
b = 20
max = {True: a, False:b} [a > b]
print(max)

# -> 20, aqui imprime el nro 20, utilizo el diccionario donde la clave
# es verdadero o falso segun la condicion a>b. Luego se selecciona el
# valor correspondiente, en este caso, como es falsa la condicion, tomas
# el valor de b, que es 20.

"""
Ternary Operator using Python Lambda
"""

a =  10
b = 20
max =(lambda x, y: x if x > y else y)(a, b)
print(max)
# -> 20


"""
Ternary Operator with Print Function
"""
a = 10
b = 20
print ("a is greater" if a> b else "b is greater")


