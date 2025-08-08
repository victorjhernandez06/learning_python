import re


"""[arn]"""
# Retuns a match where one of the specified characters (a,r,or n)is present
txt = "The rain in Spain"
#Check if the string has any a, r or n characters.
x = re.findall('[arn]', txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
    
# ['r', 'a', 'n', 'n', 'a', 'n']
# Yes, there is at least one match!
print('-'*55)


"""[a-n]"""
# Returns a match for any lower case character, alphabetically between a and n.

txt = "The rain in Cojedes"
x  = re.findall('[a-n]', txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
# ['h', 'e', 'a', 'i', 'n', 'i', 'n', 'j', 'e', 'd', 'e']
# Yes, there is at least one match!
print('-'*55)


"""[^arn]"""
# Return a match for any character Except a, r, and n.

txt = "the rain in Cojedes"
x = re.findall('[^arn]', txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
# ['t', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'C', 'o', 'j', 'e', 'd', 'e', 's']
# Yes, there is at least one match!
print('-'*55)



"""[0123]"""
# Return a match where any of the specified digits (0,1,2 or 3) are present

txt = 'The rain in Spain'
x = re.findall('[0123]', txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
# []
# No match!  
print('-'*55)


"""[0-9]"""
# Returns a match for any digit between 0 and 9.
x = re.findall('[0-9]', txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
# []
# No match!  
print('-'*55)


"""[0-5][0-9]"""
# Returns a match for any two-digit numbers from 00 and 59

txt = "08 times before 11:45 AM"
#check if the string has any two-digit numbers, from 00 to 59
x = re.findall('[0-5][0-9]',txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
# ['08', '11', '45']
# Yes, there is at least one match!
print('-'*55)




"""[a-z][A-Z]"""
# Return a match for any character alphabetically between a and z, lower case OR upper case.

txt = "08 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")
# ['t', 'i', 'm', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'A', 'M']
# Yes, there is at least one match!
print('-'*55)


"""[+]"""

# in sets +, * , . , | , (), $ , {}, has no special meaning, so [+] means, return a match for any + character in the string
import re

txt = "8 times before!! + 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[!]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# ['!', '!']
# No match