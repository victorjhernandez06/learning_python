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

print('-'*55)

"""THE FINDALL() FUCNTION"""
# The findall() function returns a list containing matches

# Example: Print a list of all matches
txt = "the rain Spain"
x =re.findall("ai", txt)
print(x)
# --> ['ai', 'ai']

# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned.


print('-'*55)

# Example: return an empty list if no match was found:

x = re.findall("portugal", txt)
print(x)

# --> []

""" THE SEARCH() FUNCTION """
 # the search() function searches the string for a match, and returns a Match Object if there is a match.

# if there is more than one match, only the first occurrence of the match will be returned:

print('-'*55)

# Example: Search for the first white-space character in the string:
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
# --> The first white-space character is located in position: 3


print('-'*55)

#if no matches are found, the value None is returned:
# Example: make a search thet returns no match:

txt = "the rain in Spain"
x = re.search("portugues", txt)
print(x)
# --> None


print('-'*55)

""" THE SPLIT() FUNCTION """
# The split() function returns a list where the string has been split at each match:
# Example: Split at each white-space charater

x = re.split("\s", txt)
print(x)
# --> ['the', 'rain', 'in', 'Spain']

print('-'*55)

# You can control the number of occurrences by specifying the maxsplit parameter:
#Example: split the string only at the first occurrence:
x = re.split("\s", txt,1)
print(x)

# --> ['the', 'rain in Spain']
print('-'*55)

""" The Sub9) function """
#the sub() function replaces the matcher with the text of your choice:
# Example: replace every white-space character with the number 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
# --> The9rain9in9Spain

# Replace the first 2 occurrences:
print('-'*55)
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# --> The9rain9in Spain

""" THE MATCH OBJECT """

# A match Object is an object containing information about the search and the result.
# Note: If there in no match, the valu None will be returned, instead of the Match Object.
print('-'*55)

#Example: Do o search that will return a Match Object:
x = re.search("ai", txt)
print(x) # this will print an object.

# The Match object has properties and methods used to retrieve information about the search, and the result:

## .span() Returns a tuple containing the start, and end positions of the match.
## .string Returns the string passed into the function.
## .group() Retuns the part of the string where there was a match.

# Example: Print the position (start - and end position ) of the first match occurrence.
# The regular expression looks for any words thet starts with an upper case "S":
x = re.search(r"\bS|w+", txt)
print(x.span()) #--> (12, 13)

# Example: print the string passed into the function
x =  re.search(r"\bS\w+",txt)
print(x.group())
# --> Spain



