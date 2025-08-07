print("hello Word",'\n---')

if 10 > 5:
    print("this is true!")
    print("I am tab indentation",'\n---')

print("I have no indentation",'\n---')

#input function return the user input in form of a string
# name = input ("escribe tu nombre:")
# print (f"tu nombre es: {name}")

#single variable
print ("Variables")
s = "victor"
print(s)

#multiple variable
s = "Alice"
age = 25
city = "Los Angeles"
print(s,age, city)

"""
Python string split()
splits a string into a list of string after breaking the given 
by the specified separator

El metodo split() de python divide una cadena en una 
lista despues de romper la cadena dada con el separador especifico
"""
string = "one, two, three"
words =  string.split(',')
print (words)
#-> ['one', ' two', ' three']

#splits
text = 'geeks for geeks'
#plits at space
print(text.split())
#-> ['geeks', 'for', 'geeks']

word = 'geeks, for, geeks'
#split at ','
print(word.split(','))
#-> ['geeks', ' for', ' geeks']

word = "geeks:for:geeks"
#pliting at ':'
print(word.split(':'))
#->['geeks', ' for', ' geeks']

word = 'CatBatSatFatOr'
#spliting at t
print(word.split("t"))
#->['Ca', 'Ba', 'Sa', 'Fa', 'Or']

# How does split() work when maxsplit is specified?


