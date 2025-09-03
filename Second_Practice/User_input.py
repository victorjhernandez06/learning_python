"""Python User Input"""

# That means we are able to ask the user for input
# The following example asks for your name, and when you enter a name, it gets printed on the screen

# Example: Ask for user input:
print("Enter  your name: ")
name = input()
print(f"hello m{name}")

# Python stops executing when it comes to the input() function, and continues when the user has given some input.

"""USING PROMPT"""
# In the example above, the user had to input their name on a new line. The Python input() function has a prompt parameter, which acts as a message you can put in front of the user input, on the same line.

#Example: Add a message in front of the user input.
name = input("Enter your name: ")
print(f"Hello {name}")

"""Multiples Inputs"""

#you can add as many inputs as you want, Python will stop executing at each of them, waiting for user input.

#Example: Multiple inputs.