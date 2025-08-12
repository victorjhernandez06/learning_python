my_string =  "My string"
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

# el \n es un salto de linea
my_new_line_string = "este es un String \ncon salto de linea"
print(my_new_line_string)

# \t es una tabulacion
my_tab_string = "este es un String \tcon tabulacion"
print(my_tab_string)

#para escapar de los \n y \t, le coloco una \ extra para dejar sin efecto estas instrucciones.. 

#Como formatear los String.
name, surname, age= "Victor", "Hernandez", 42
print('Mi nombre es %sname %ssurname y mi edad es %dage')

# %s -> le paso un string
# %d -> le paso un entero
# %f -> le paso un float
dvs = '------------------------------'
print(dvs)
# este formato sirve cuando internacionalicemos la edad. 
#esta forma es optima cuando tenemos formatos diferentes
print ("Mi nombre es {} {} y mi edad es: {}".format(name, surname, age)) 

#esta forma es mucho mas rapida, pero debemos tomar en cuenta si es %s para string %d para enteros
#Esta es una de las formas optimas.
print ("mi nombre es %s %s y mi edad es: %d" %(name, surname,age)) 

#forma menos convencional para novatos. 
print("Mi nombre es" + name + " " + surname + " " + "y mi edad es: " + str(age))

#colocamos la f, para formatear los datos y que el programa sabe si es un string. la f sirve para formatear.
#Esta es una de las formas optimas.
print(f"Mi nombre es {name} {surname} y mi edad {age}")

#desempaquetados de caracteres

language = "Python"
a, b, c, d, e, f = language
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)


#division
print(dvs)
language_slice = language[1:3]
print (language_slice)


#Reverse
print(dvs)
reverse_language = language [:: -1]
print(reverse_language)


#metodos o funciones del sistema
print(dvs)
print(language.capitalize())
print(language.casefold())
print(language.center(20, "*"))
print(language.count("o"))
print(language.endswith("n"))
print(language.expandtabs(tabsize=4))
print(language.find("o"))
print(language.format())
print(language.index("o"))
print(language.upper())
print("1".isnumeric)
