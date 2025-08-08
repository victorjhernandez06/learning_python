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

"""[0-9]"""
# Returns a match for any digit between 0 and 9.

"""[0-5][0-9]"""
# Returns a match for any two-digit numbers from 00 and 59


"""[a-z][A-Z]"""
# Return a match for any character alphabetically between a and z, lower case OR upper case.

"""[+]"""

# in sets +, * , . , | , (), $ , {}, has no special meaning, so [+] means, return a match for any + character in the string