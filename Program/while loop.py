"""Python While Loop"""

# Infinite while Loop in Python
# While loop with continue statements

# Print all letters except 'e' and
i = 0
a = 'Victor Hernandez'
while i < len(a):
    if a[i] == 'e' or a[i] == 'H':
        i += 1
        continue
    print (a[i])
    i += 1

"""while loop with break statement"""

i = 0
a = 'Mathias Hernandez'

while i < len(a):
    if a[i] == 'a' or a[i] == 's':
        break
    print (a[i])
    i +=1

# -> M, porque se corta en la primera coincidencia.


"""while loop with pass statement"""

#An empty loop

a = "Sofia Victoria"
i = 0

while i < len(a):
    i += 1
    pass

print('Value of i:', i)
# -> Value of i: 14

"""while loop with else"""
i = 0
while i < 4:
    i += 1
    print(i)
else: #Executed because no break in for
    print('No Break\n')

i = 0
while i < 4:
    i += 1
    print(i)
    break
else: #Not executed as there is a break
    print("No Break")

