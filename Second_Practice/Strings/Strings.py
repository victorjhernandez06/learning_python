# Python Strings
#Strings in python are sourronded by either single quotation marks, or double quotation marks
# "Hello" is the same as 'Hello'
# We can display a string literal with the print() function
print("Hello")
print('Hello')

#Quotes inside Quotes
#Yoy can use quotes inside a string as long as they don't match the quotes aurrounding the string the string

print("It's a nice day")
print('She said "Hello"')
print('He is called "Victor"')

#Assign String to a Variable
a = "Hello Victor"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes
a = """ Aqui puedo escribir un texto,
dar enter y poder escribir en la linea siguiente
sin que se rompa el codigo"""

# Or Three single Quotes
b = ''' Aqui puedo escribir un texto,
dar enter y poder escribir en la linea siguiente
sin que se rompa el codigo'''
print(a)
print(b)

#String are Arrays
# like many other popular programming languages, strings in python are arrays of bytes representing unicode characters
# However, python does not have a character data type, a single character is simply a string with a length of 1
# Square brackets can be used to access elements of the string

c = "Hello Victor"
print(c[1])

#Looping through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop
for x in "Hernandez":
    print(x)
    

#String Length
# To get the length of a string, use the built-in len() function
# Para obtener la longitud de una cadena, use la función incorporada len()
d = "Hello karina"
print(len(d))

#Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in
# Para verificar si una cierta frase o carácter está presente en una cadena, podemos usar la palabra clave in
txt = "The best things in life are free!"
print("free" in txt)
print("best" in txt)


