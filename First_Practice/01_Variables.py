# Variables
myVariable = "My String variable"


my_variable = "Second way of writing variable"
print(myVariable)
print(my_variable)


#Podemos usar todos los valores primitivos de una variable.

myStringVariable = "string"
print(type(myStringVariable))
my_bool_variable = True
print(my_bool_variable)
myIntVariable = 4
print(myIntVariable)

print(myStringVariable, my_bool_variable, myIntVariable)

my_str_change = str(myIntVariable)
print(my_str_change)
print(type(my_str_change))

#concatenacin de variables en un print.
print(myStringVariable, myIntVariable, my_bool_variable)
print(type(print(myStringVariable, myIntVariable, my_bool_variable)))


#funciones del sistema
#len() devuelve la cantidad de caracteres de una cadena.
print(len(myStringVariable))

#lower() devuelve una cadena en minúsculas.
print(myStringVariable.lower())

#upper() devuelve una cadena en mayúsculas.
print(myStringVariable.upper())


#capitalize() devuelve una cadena con la primera letra en mayúscula y el resto en min
#usculas.
print(myStringVariable.capitalize())


#count() devuelve la cantidad de veces que aparece un caracter en una cadena.
print(myStringVariable.count('i'))


#find() devuelve la posición del caracter en una cadena.
#si no lo encuentra devuelve -1.
print(myStringVariable.find('i'))


#format() devuelve una cadena con los valores de una lista.
#El primer valor de la lista es el primer valor de la cadena, el segundo valor de la
#lista es el segundo valor de la cadena, etc.
print(myStringVariable.format(myIntVariable, my_bool_variable))


#join() devuelve una cadena con los valores de una lista.
#El valor de la lista es el caracter que se utiliza para unir los valores de la lista
#en una cadena.
print(' '.join(['hola', 'mundo']))


#lstrip() devuelve una cadena sin el caracter que se le pasa como argumento en el
#lado izquierdo.
print(myStringVariable.lstrip('h'))


#rstrip() devuelve una cadena sin el caracter que se le pasa como argumento en el
#lado derecho.
print(myStringVariable.rstrip('g'))


#split() devuelve una lista con los valores de una cadena.
print(myStringVariable.split(' '))


#strip() devuelve una cadena sin el caracter que se le pasa como argumento en los
#lados izquierdo y derecho.
print(myStringVariable.strip('h'))


#str() devuelve una cadena con el valor de un objeto.
print(str(myIntVariable))


#Variables de una sola linea !cuidado con abuso de esta sintaxis.
name, surname, alias, edad = "Victor","Hernandez",'VictorDev06', 41
print("Me llamo:",name, surname,",","Mi alias es:", alias,"y tengo:",edad)

#SCOPE VARIABLES

def f():
    a = "Variable Local"
    print(a)

f()
#Variable local, imprime print(a) # this would raise since 'local_va' is not accesible outside the fucntion
# Esto generaria un error ya que 'Local var' no es accesible fuera de la funcion.
#Variables defined outside any function are global and can be accessed inside functions using the global keyword.
#Las Variables definidas fuera de cualquier funcion son globales y se puede acceder a ellas dentro
# de las funciones utilizando la palabra clave global.

a = "Variable global"

def f():
    global a
    a = "Modified Globally"
    print(a)

f()
#modified globally
print(a)
#Modified Globally

#Aqui se introdujo la variable global dentro del scope de la funcion, y desde adentro
# la variable a fue modificada y adopta el valor que tiene en el scope de la funcion.

# Delete a variable using DEL keyword
#del removes the variable from memory.

#assigning value to variable
x = 10
print(x)

#removing the variable using del.
del x
#Trying to print x, after deletion will raise a error


#EXAMPLES
a, b =  5, 10
a, b = b, a
print ("a ->",a)
print (f"b -> {b}")
print (a, b)

#counting Characters im a String
word = "Python"
length = len(word)
print(f"length of the word: {length}")
print("La longitud de la variable es:", length)


