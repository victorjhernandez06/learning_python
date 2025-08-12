"""
LAS VARIABLES
## Son contenedores, que nos sirven para guardar ciertos tipos de datos.
## Son dinámicamente tipadas.
## También se pueden especificar por un tipo de dato por ejemplo INT, FLOAT, BOOLEANS, STRING
## Con la function TYPE, podemos obtener el tipo de cada variable.
## Los nombres deben empezar con una letra Mayúsculas o Minuscules o con un guion
## También podemos usar el nombre CamelCase, o variables largas divididas con guiones Bajos

"""

age = 16
name = "Adrian de jesus"
print (age)
print (name)

age = "Modificando la variable edad por string"
print(age)

number = int(10)
number_float = float(10)

print(number, number_float)
print (type(number_float))
print(type(number))