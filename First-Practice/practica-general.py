#Numbers

p1 = 2
p2 = 2
print(p1 + p2)

print(50 - 5 * 6)

print( (50 - 5*6) / 4)

print(8 / 5) #division always returns a floating-point number

print(17 /3) #classic division returns a float

print(17 // 3) #floor division discards the fractional part

print(17 % 3) # the operator returns the remainder of the division

print(5*3+2) # floored quotient * divisor + remainder

print(5 ** 2) # squared

print(2 ** 7) # 2 to the power of 7

width = 20
height = 5 * 9
print(width * height)

tax = 12.5 / 100
price = 100.50
print(price * tax)

#text

print('spam eggs')
print ('Doesn\'t') # use \' to escape yhe single quote
print("Doesn't") #...or use double quotes instead

print ('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Ins\'t," "they said')

s = 'First line.\nSecond Line.' # \n means newline
print (s) # with print(), special characters are interpreted, so \n produces new line


print(r'c:\some\name') # note the r before the quote


print("""\
... Usage: thingy [OPTIONS]
... h     Display this usage message
... H hostname  Hostname to conect to
""")

print( 3* 'vic' + 'tor')
print('Py''thon')


text = ('Put several string within parentheses '
        'to have them joined together.')
print(text)

prefix = 'Py'
# prefix 'thon' #can't concatenate a variable a string literal
print ('un'*3 + 'ium')

#concatenate variables or variable and a literal, use +
print(prefix + 'thon')
# -> Python

#string can be indexed (subscripted), with the first characters having index 0. there is no separate character type; a character is simply string of size one

word = "Python"
print(word[0]) # character in position 0
# -> P
print(word[5])
#-> n

# Indices may also be negative numbers, to start counting from the right:
print(word[-1]) # Last Character n
print(word[-2]) # Second-later character o
print(word[-6]) # the first character P

# note that since -0 is the same 0, negative indices start from -1
print (word[0:2]) # Characters from position 0 (included) to 2 (excluded)
print (word[2:5]) # Characters from position 2 (included) to 5 (Excluded)

# Slice indices have useful defaults: an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced

print(word[:2]) # Characters from the beginning to position 2 (excluded). #-> Py
print(word[4:]) # characters from the 4 (included) to the end. #-> on
print(word[-2:]) # Characters from the second-last (included) to the end. #-> on

#  Note: how the start ins always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

print(word[:2] + word[2:]) #-> Python
print(word[:4] + word[4:]) # -> Python

# THEY STRING IN PYTHON are IMMUTABLE
# word[0] = 'J' --> TypeError: 'str' object does not support item assignment
print(word)

# if you need a different string, you should create a new one
word = 'javascript'
print(word)
# Puedo cambiar la variable de manera completa, no parte de ella.

""" 
### LIST ###
Python knows a number of compound data types, used to group together other values. the mos versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. list might contain items of different types, but usually the items all have the same type 
"""

squares = [1,4,9,16,25]
print (squares)
# like strings(and all other built-in sequence types), list can be indexed and sliced

print(squares[0]) # indexed returns the item 1
print(squares[-1]) # show the last item --> 25
print(squares[-3:]) # Slicing returns a new list --> [9,16,25]

# list also support operations like concatenation:
print(squares + [36, 49, 64, 81, 100])

# Unlike string, which are immutable, list are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125] # something's wrong
print(4 ** 3) # the cube of 4 is 64, not 65
cubes[3] = 64 # replace the wrong value
print(cubes)  # --> [1, 8, 27, 64, 125]

# You can also add new items at the end of the list, by using the list.append()
cubes.append(216)
cubes.append(7**3)
print(cubes) # --> [1, 8, 27, 64, 125, 216, 343]

# Simple assignment in python never copies data. When you asign a list to variable, the variable refers to the existing list. Any changes you make to the list through one variable will be seen through all other variables that refer to it:

rgb = ['Red', 'Green', 'Blue']
rgba = rgb
print(id(rgb) == id(rgba)) # they reference the same object --> True

rgba.append("Alph")
print(rgb) # --> ["Red", "Green", "Blue", "Alph"]

# All slice operations return a new list containing the requested elements. this means that the following slice returns a shallow copy of the list.

correct_rgba = rgb[:]
correct_rgba [-1] = "Alpha"
print(correct_rgba) # --> ['Red', 'Green', 'Blue', 'Alpha']
print(rgba) # --> ['Red', 'Green', 'Blue', 'Alph']

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# Replace some values
letters [2:5] = ['C', 'D', 'E']
print (letters)  # --> ['a', 'b', 'C', 'D', 'E', 'f', 'g']

#Now Remove them
letters[2:5] = []
print (letters) # --> ['a', 'b', 'f', 'g']

#clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters) # --> []

# the built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print(len(letters)) #--> 4

# It is possible to nest list (create list containing other list)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a,n]
print(x) # --> [['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) # --> ['a', 'b', 'c']

print(x[0][1]) # --> b

# fibonacci series:
# the sum of two elements defines the next

a , b = 0, 1
while a < 100:
        print(a)
        a,b = b, a+b

i = 256 * 256
print('the value of i is:', i)

a,b = 0, 1
while a<1000:
        print(a, end=',')
        a, b = b, a+b

