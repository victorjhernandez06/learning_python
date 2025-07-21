"""
Python – Dictionary values String Length Summation
Sumatoria de los caracteres de valores dentro de los diccionarios.
"""

"""
Method #1: Using sum() + generator Espression + len()
the comination of above functions can be used to perform this task.
"""

#Using sum() + len() + generator expression

#initializing dictionary
test_dict = {
    'Victor' : 'father',
    'Karina' : 'Mother',
    'Adrian' : 'First Child',
    'Mathias' : 'Second child',
    'Sofia' : 'Third Child'
}

#printing original dictionary
print("The original dictionary" + str(test_dict))
#-> The original dictionary{'Victor': 'father', 'Karina': 'Mother', 'Adrian': 'First Child', 'Mathias': 'Second child', 'Sofia': 'Third Child'}
#Dictionary values string length summation
##Using sum() + len() + generator expression
res = sum(len(val) for val in test_dict.values())
print("The string values length summation is: "+ str(res))
#-> The string values length summation is: 46


"""
Method #2: Using map() + len() + sum()
The only diference is that iteration is performed using map() than generator expression.
"""
#Using the same dictionary call test_dict
#Print the original dictionary
print('The original dictionary :' + str(test_dict))

#using map() + len() + sum()
res = sum(map(len, test_dict.values()))
print ("The string values length summation :" + str (res))
# -> The string values length summation :46

"""
Method #3: Using a for loop
"""

#Same dictionary test_dict
print("The original dictionary :"+ str(test_dict))

#Using for loop
res = 0
for val in test_dict.values():
    res += len(val)
print(" The string values length summation:"+ str(res))
# -> The string values length summation:46