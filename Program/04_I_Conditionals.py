"""Conditionals"""
# from numpy.ma.core import true_divide

"""
IF, ELSE, ELIF
"""

"""
ElSE
"""
# print('Verificacion de acceso')
# edad_usuario = int(input('Introduce tu edad por favor'))
#
# if edad_usuario<18:
#     print("No puede pasar")
# print('Puedes pasar')

age = 20
if age >= 18:
    print("Elegible to vote")

# -> Eligible to vote.

i =20
#checking if i is greater tha 0
if (i > 0):
    print("i is positive")
else:
    print("i is 0 or negative")
# -> i is positve

"""
If Else in One-line
"""

a = -2
#ternay conditional to check if number is positive or negative
res  = "positive" if a >= 0 else "negative"
print(res)

# -> Negative

"""
Short Hand if
"""

age = 19
if age >18: print("Elegible to vote")


"""
If else Conditional Statements in Python
"""
age = 10
if age <=12:
    print("travel for free")
else:
    print("pay for tickets")

# -> travel for free


"""
Short Hand if-else
"""
marks = 45
res = "Pass" if marks >= 40 else "fail"
print (f"Result: {res}")

# -> Result: Pass


"""
elif Statement
"""

age = 25
if age <=12:
    print("child")
elif age <=19:
    print("teenager")
elif age <= 35:
    print("Young Adult")
else:
    print("Adult")

"""
Nested if..else Conditional Statements in Python
"""
age = 60
is_number = True

if age >= 60:
    if is_number:
        print("30% senior discount!")
    else:
        print("20% senior discount!")
else:
    print("Not elegible for a senior discount")
# -> 30% senior discount!

"""
Ternary Conditional Statement in Python
"""

#asign a value assed on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)
# -> Adult

"""
Match-Case Statement in Python
"""
# Is a version a switch - case found in other languages.

number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or three")
    case _:
        print("Other number")

# -> Two or Three

"""
Python If Else Statements – Conditional Statements
If statement
"""

i = 10
#checking if i is greater than 15
if(i > 15):
    print("10 is less than 15")

print("I am not in if")
# -> I am not in if.

"""
Logical Operators with If..Else
"""

age = 25
exp = 10

#using ">" operator & 'and with if-else
if age > 23 and exp > 8:
    print("Elegible.")
else:
    print("Not Elegible.")
# - >  Elegible


"""
Nested if Else Statement
"""

i = 10
if ( i == 10):

    #first if statement
    if(i < 15):
        print("i is smaller than 15")

    # nested - if statement
    # Will only executed if stetement above
    # it is true
    if(i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

else:
    print('i is not equal to 10')

# -> i is smaller than 15
# -> is smaller than 12 too

# Example 2

i = 25
    #checking if i is equal to 10
if ( 1 == 10):
    print("i is 10")

    #checking if is equal to 15
elif ( i == 15):
    print("i is 15")

    #checking if i is equal to 20
elif ( i == 20):
    print( "i is 20")

    #If none of the above conditions are true
else:
    print(' i is not present')

# -> i is not present


# Problems
"""
There are two friends, John and Smith, and the parameters j_angry and s_angry 
to indicate if each is angry. You are in trouble if both of them are angry or 
no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false
"""

#Solutions
#input
j_angry = True
s_angry = True

#output -> True
if (j_angry == True) and (s_angry == True):
    print("Since both of them are angry, you are in trouble.")
elif (j_angry == True) and (s_angry == False):
    print("Only one of them is angry, you are not in trouble.")
else:
    print("nothing happen")

def friends_in_trouble(j_angry, s_angry):
    if j_angry == True and s_angry == True:
        return True

print(friends_in_trouble(j_angry,s_angry))

