dictionary = {
    'Programar' : 'Programar es transformar el cafe en codigo',
    'POO': 'Programacion Orientada a Objetos',
    "MVC": "Modelo Vista Controlador"
 }

print(dictionary['POO']) # --> Programacion Orientada a Objetos
print(dictionary['MVC']) # --> Modelo Vista Controlador

# Escribir un numero y transformarlo a su equivalente en texto

numbers={
    '0': 'Cero',
    '1':'Uno',
    '2':'Dos',
    '3':'Tres',
    '4':'Cuatro',
    '5':'five',
    '6':'Six',
    '7':'Seven',
    '8':'Eighth',
    '9':'Nine'
}
# escribir un  y no vamos a escribir en texto
texto = input("ingrese un numero: ")

textofinal = ''
for letter in texto:
    textofinal += numbers.get(letter, f'"{letter}" este item, no esta en el rango') + ' '
    print(letter)

print(textofinal)
print(" ")

textofinal2 = ""
for letter in texto:
    textofinal2 = textofinal2 + numbers.get(letter, '?') + ' '

print(textofinal2)

"""ENCRIPTAR INFORMACION CON PYTHON"""
tarjeta_de_credito: 344-1223-23323
codigo_de_seguridad: 323

tarjeta_de_credito: 344-1223-23323
codigo_de_seguridad: 323

email: victor1@gmail.com
pass: victor112233*