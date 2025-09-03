"""F-String"""
# F-string allows you format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal, like this.

# Create an f-string
txt = f"the price is 49 dollars"
print(txt)

# a placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon: followed by a legal formatting type, like 2.f which means fixed point number with 2 decimals.

# Example: Display the price with 2 decimals:
price =  59
txt = f"the price is {price:.2f} dollars"
print(txt)

# You can also format a value directly without keeping in a variable
# Example: Display tha value 95 with 2 decimals

txt = f"the price is {95:.2f} dollars"
print(txt)

"""PERFORM OPERATIONS IN F-STRING"""
# You can perform Python operations inside the placeholders.
# You can do math operations.

#Example Perform a math operation in the placeholder, and return the result:
txt = f"the price is {20 * 59} dollars"
print(txt)

# You can perform math operations on variables

# Example: add taxes before displaying the price:

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# You can perform if...else statements inside the placeholders:
# Example "Expensive" if the price is over 50, otherwise return "Cheap":

price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

"""EXECUTE FUNCTIONS IN F-STRINGS"""
# You can execute functions inside the placeholders:
# Use the string method upper() to convert a value into upper case letters:
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# The function does not have to be a built-in Python method, you can create your own functions and use them:
# Example: Create a function that converts feet into meters:
def myconvert(x):
    return x * 0.3048

txt = f"The place is flying at a {myconvert(20)} meter altitude"
print(txt)

"""MORE MODIFIERS"""
#  At the beginning of the chapter we explained how to use the .2f modifier to format a numer into a fixed point number with 2 decimals.
# There are several other modifiers that can be used to format values:

# Example: Use a comma as a thousand separator
price = 59000
txt = f"The price is a {price:,} dollars"
print(txt)

# Here is a list of all the formatting types
# "<"
# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
# Use "<" to left-align the value:
txt = f"We have {49:<8} chickens"
print(txt)

#Rigth aligns the result (Within the available space)
# ">"
# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
# Use ">" to left-align the value:
txt = f"We have {49:>8} chickens."
print(txt)

# Center aligns the result (within the available space)
# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = f"We have {49:^8} chickens."
print(txt)

# Places the sign to the left most position
# Center aligns the result (within the available space)
# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "=" to place the plus/minus sign at the left most position:
txt = f"We have {-5:=8} chickens."
print(txt)


# Use a plus sign to indicate if the result is positive or negative
#Use "+" to always indicate if the number is positive or negative:
txt = f"The temperatures is between {-3:+} and {7:+} degrees celsius"
print(txt)

# Use a minus sign for negative values only
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = f"The temperatures is between {-3:-} and {7:-} degrees celsius"
print(txt)

#U se " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = f"THe temperature is between {-3: } and {7: } degrees celsius."
print(txt)

# Use a comma as a thousand separator
#Use "," to add a comma as a thousand separator:
txt = f"The universe is {138000000:,} years old."
print(txt)

#Use a underscore as a thousand separator
#Use "_" to add a underscore character as a thousand separator:
txt = f"The universe is {138000000:_} years old."
print(txt)

#Binary format
#Use "b" to convert the number into binary format:
txt = f"The binary version of 5 is {5:b}"
print(txt)

#Decimal format
#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = f"We have {0b101:d} chickens"
print(txt)

# Scientific format, with a lower case e
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = f"We have {5:e} chickens"
print(txt)


# Scientific format, with an upper case E
# Use "E" to convert a number into scientific number format (with an upper-case E):
txt = f"We have {5:E} Chickens"
print(txt)

#Fix point number format
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = f"The price is {45:.2f} dollars."
print(txt)

#without the ".2f" inside the placeholder, this number will displayed like this:
txt = f"The price is {45:f} dollars."
print(txt)

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')
txt = f"The price is {x:F} dollars"
print(txt)


"""STRING FORMAT()"""
# The format(), method can still be used, but f-string are faster and the preferred way to format strings.
# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly

# Example: Add a placeholder where you want to display the price:
price = 49
txt =  "The price is {} dollars"
print(txt.format(price))

# You can add parameters inside the curly brackets to specify how to convert the value:

txt = "The price is {:.2f} dollars"
print (txt.format(price))

#check out all formating types in our String format() reference.

"""Multiple Value"""
#If you want to use more values, just add more values to the format(). method.
# print(text.format(price, itemno, count))

# and add more placeholders
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

"""INDEX NUMBERS"""
# you can use index numbers(a number inside the curly brackets {0} to be sure the values are placed in the correct placeholders.
quantity = 4
itemno = 568
price = 50
myorder = "I want {0} pieces of items number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#also if you want to refer to the same value more than once, use the index number:

age = 42
name = "Victor"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

"""NAMED INDEXES"""
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameters values txt.format(carname ="Ford"):

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

