"""CONDITIONALS"""
# Python Conditions and If statements
### Conditions IF

my_conditions =  True

if my_conditions == True:
    print("la condicion se ejecuta la condicion del if")

print("la condicion no se ejecuta")


# Es la tercera vez que lo hagosource venv/bin/activate
my_conditions = 5*2*3

if my_conditions == 20:
    print(f"The value in my conditions is {my_conditions}")
elif my_conditions == 10:
    print(f"The value in my conditions is {my_conditions}")
else:
    print(f"The value in my conditions is {my_conditions}")


# Short hand if..else
a = 2
b = 330

print("A") if a>b else print("B") #--> B

a = 200
b = 33
if b > a:
    print("B is greater than A")
else:
    print("A is greater than B")
    
    
# Short Hand If
if a>b: print ("A is greater than B")

# This technique is known as Ternary Operators, or Conditional Expressions.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

"""AND"""
# the AND keyword is a logical operator, and is used to combine conditionals statements.
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True") #Ambas condiciones tienen que cumplirse.
    
"""OR"""
a = 200
b = 34
c = 550
if a > b or a > c:
    print("At least one of the conditions is True") # Al menos una condicion debe cumplirse.
    
"""NOT"""
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

# test if a NOT grater than b.
a = 33
b = 200
if not a > b:
    print("a is a NOT greater than b")

"""Nested If""" # Si Anidado
# You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

"""THE PASS STATEMENT"""
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
    pass

# Exercise
x = 5
y = 8
if x > y:
    print("Hello")
else: 
    print("Welcome")
    
    



