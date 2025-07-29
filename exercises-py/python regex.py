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
# . Any characters (except newline character) --> "he..o"
