"""Python File Write"""
"""Write to an Existing File"""

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file.
# "w" - Write - will overwrite any existing content.

# Example: Open the file "pg345.txt" a append content to the file

with open("pg345.txt", "a") as f:
    f.write("now the file has more content!")

# Open and read the file after the appending:
with open('pg345.txt') as f:
    print(f.read())


"""Overwrite Existing Content"""
# To overwrite the existing content to the file, use the w parameter:
# Example:  Open the file "pg345.txt" an overwrite the content:
with open('pg345.txt','w') as f:
    f.write("Wooops! i have deleted the content!")

#open and read the file after the overwriting:
with open("pg345.txt") as f:
    print(f.read())

"""Create the new file"""
# To create a new file in Python, use the open() method, with one of the following parameters.
# "x" Create = will create a file,  returns an error if the file exists.
# "a" Append - will create a file if the specified file does not exists.
# "w" Write create a file if the specified files does not exists.

# Example: create a new file called 'myfile.txt'
f = open('pg345.txt')

# Result: a new empty file is created.