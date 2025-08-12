""""Python RegEx"""
# a regex, orr regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

"""RegEx Module"""
# Python has built-in package called re, which can be used to work with Regular Expressions.

# Import the re module
import re

"""RegEx in Python"""
# when you have imported the re module, you can start using regular expressions.
# Example: Search the string to see if it starts with "Thee" and ends with "Spain":

txt = "the rain in Spain"
x = re.search("^The.*Spain$", txt)

"""RegEx Functions"""
# The re module offers a set of functions that allows us to seacrh a string for a match.

#Function  ---> Description
#findall --> Returns a list containing all matches

#Search --> Returns a Match Object if there is a match anywhere in the string.

#Split --> Returns  list where the string has been split at each match.

#Sub --> Replaces one or many matches with a string.

"""Metacharacters"""
# Metacharacters are characters with a special meaning

# [] --> A set characters --> "[a-m]"
# \ signals a special sequence (can also be used to escape to special characters) --> "\d"
# . --> Any characters (except newline character) --> "he..o"
# ^ --> Ends with --> "^hello"

txt = "the rain in Spain"

# find all lower case characters alphabetically between "a" and "m"
x = re.findall('[a-m]', txt)
print(x) #--> ['h', 'e', 'a', 'i', 'i', 'a', 'i']

txt2 = "That will be 59 dollars"
#Find all digit characters:
x1 = re.findall("\d", txt2)
print(x1) #--> ['5', '9']

txt3 = "hello planet"
#Search for a sequence that starts with "he" followed bt two (any) characters, and "0"
x2 = re.findall("he..o",txt3)
print(x2) #--> ['hello']

txt4 = "hello planet"
#Check if the string starts with 'hello':
x3  = re.findall("^hello", txt4)
if x3:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")
# --> Yes, the string starts with 'hello' <-- #

txt5 = "hello planet"
#check if the string ends with 'planet'
x4 = re.findall("planet$",txt5)
if x3:
    print("Yes, the string starts with 'planet'")
else:
    print("No match")
# --> Yes, the string starts with 'planet' <-- #

txt6 = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more (any) characters, and an "o"
x5  = re.findall("he.*o",txt6)
print(x5)
# --> ['hello'] <-- #

txt7 = "hello planet"
#Search for a sequence that starts with "he" followed by 1 or more (any) characters, and an "o"
x6 = re.findall("he.+o",txt7)
print(x6)
# --> ['hello'] <-- #

txt8 = "hello planet"
#Searcch for a sequence that starts with "he" followed by 0 by 1 (any) character, and an "o"
x7 = re.findall("he.?o",txt8)
print(x7)
# --> [] <-- #

text9 = "hello planet"
#Search for a sequence that starts with "he" followed exactly 2(any) characters, and an "o"
x8 = re.findall("he.{2}o",text9)
print(x8)
# --> ['hello'] <-- #

txt10 = "The rain in Spain falls mainly in the plain!"
# Check if the string contains either "falls" or "stays":
x9 = re.findall("falls|stays", txt10)
print(x9)
if x9:
    print("Yes, there is at least one match!")
else:
    print("No match")

# --> ['falls'] <-- #
# --> Yes, there is at least one match! <-- #

"""Flags"""
# You can add flags to the pattern when using regular expressions.
import re

txt = "Åland"

#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))

#Without the flag, the example would return all character:
print(re.findall("\w", txt))

#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))

text = "The rain in Spain"
#Use a case - insensitive search when finding a match for Spain in the text:
print(re.findall("spain",txt,re.DEBUG))
# LITERAL 115
# LITERAL 112
# LITERAL 97
# LITERAL 105
# LITERAL 110
#
#  0. INFO 16 0b11 5 5 (to 17)
#       prefix_skip 5
#       prefix [0x73, 0x70, 0x61, 0x69, 0x6e] ('spain')
#       overlap [0, 0, 0, 0, 0]
# 17: LITERAL 0x73 ('s')
# 19. LITERAL 0x70 ('p')
# 21. LITERAL 0x61 ('a')
# 23. LITERAL 0x69 ('i')
# 25. LITERAL 0x6e ('n')
# 27. SUCCESS

txt = """ Hi
me 
name
is 
Sally"""
#Search for sequence that starts with "me" followed by one character, even a newline charactarer, and continues with "is":
print(re.findall("me.is", txt, re.DOTALL))
# ['me\nis']
#This example would return no match without the re.DOTALL flag:
print(re.findall("me.is", txt))
# []
#Same result with the shorthand re.S flag:
print(re.findall("me.is", txt , re.S))
# ['me\nis']



txt = "The rain in Spain"
#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt , re.IGNORECASE))
# ['Spain']
#Same result using the shorthand re.I flag:
print(re.findall("spain",txt, re.I))
# ['Spain']


txt = """there
aint much
rain in 
Spain"""

#Search for the sequence 'ain', at the begining of a line:
print(re.findall("^ain", txt, re.MULTILINE))
# --> ['ain']
#This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning fo the text:
print(re.findall("^ain", txt))
# --> []
#Same result with the shorthand re.M flag:
print(re.findall("^ain", txt, re.M))
# --> ['ain']

txt = "Victor"
#Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE))
# ['V', 'i', 'c', 't', 'o', 'r']
#same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U))
# ['V', 'i', 'c', 't', 'o', 'r']


txt = "The rain in Spain falls mainly on the plain"
#find and return words that contains the phrase "ain":

pattern = """
[A-Za-z]    #starts with any letter
ain+        #contains 'ain'
[a-z]*      #followed by any small letter
"""
print(re.findall(pattern,txt,re.VERBOSE))
# ['rain', 'pain', 'mainly', 'lain']

#The examle woud return nothing without the re.VERBOSE flag
print(re.findall(pattern,txt))
# []

#Same result woth the shorthand re.X flag;
print(re.findall(pattern,text, re.X))
# ['rain', 'pain']



"""Special Sequences"""
# A special sequence is a \ followed by one of the characters in the list bellow, and has special meaning.

txt = "The rain in Spain"
#check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
    print("Yes,  there is a match")
else:
    print("No match")

# ['The']
# Yes,  there is a match


# Returns a match where the specified characters are the beginning or at the end of a word.
txt =  "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)
if x:
    print("Yes, there is at last one match!")
else:
    print("No match")
# []
# No match

# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
x = re.findall(r"in\b", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# ['in', 'in', 'in']
# Yes, there is at least one match!

"""\B"""
# Returns a match where the specified charaters are present,but NOT at the beginning (or at the end) of a word.

txt = "The rain in Spain"
#Check if "ain" is present,but NOT at the beginning of a word.
x = re.findall(r"\Bain",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("no match")

txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# (The "r" in the beginning is making sure that the string is being treated as a "raw string"

"""\d"""
# Returns a match where the string contains digits (numbers from 0-9)
txt11 = "the rain in Spain 01"
# Check if the string contain any figits (number from 0-9)
x = re.findall("\d",txt11)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("no match!")

# ['0', '1']
# Yes, there is at least one match!


"""\D"""

#Returns a match where the string DOES NOT contain digits.

txt = "The rain in Spain"

#return a match at every no digit character:

x = re.findall("\D",txt)
print(x)
if x:
    print('Yes, there is at least one match!')
else:
    print("No match")
#--> ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
#--> Yes, there is at least one match!

"""\s"""
# Returns a match where the string contains a white space character

txt  =  "the rain in Spain"
#Return a match at every white-s[ace characters:

x = re.findall("\s",txt)
print(x)
if x:
    print('Yes, there is at least one match!')
else:
    print("No Match")

# [' ', ' ', ' ']
# Yes, there is at least one match!


"""\S"""
# Returns a match where the string DOES NOT contain a white space characters

txt = "The rain in Cojedes"
#Return a match at every NON white-space character:
x = re.findall("\S",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No Match")

# ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'C', 'o', 'j', 'e', 'd', 'e', 's']
# Yes, there is at least one match!

"""\w"""
# Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9 and underscore _character)

txt = "the rain in Spain"
# Return a match at every word characters(Characters from a to Z, digits from 0-9, and the underscore _Characters)

x = re.findall("\w",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# ['t', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
# Yes, there is at least one match!


"""\W"""
# Returns a match where the string DOES NOT contain any word characters

txt = "the rain in Spain"
# Return a match at every NON word Character (characters NOT between a and Z, like "!", "?" thite space, etc...)

x = re.findall("\W", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


"""\Z"""  # "Spain\Z"
# Returns a match fi the specified characters are at the end of the string. 

txt =  "The rain in Cojedes"
# Check if the string ends with "Cojedes"

x = re.findall("Cojedes\Z", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    
# ['Cojedes']
# Yes, there is at least one match!

