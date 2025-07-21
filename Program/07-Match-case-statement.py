
"""
Python Match Case Statement
"""

def check_number (x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case 2:
            print("It's 2")
        case _:
            print("It's neither 10 nor 20")

check_number(10)
check_number(19)
check_number(2)

"""
Match Case Statements with Constants
Hacer coincidir declaraciones de caso con Constantes. 
"""

def greet (person):
    match person:
        case "A":
            print("Hello, A!")
        case "B":
            print("Hello, B!")
        case ("Victor"):
            print("Hola Victor")
        case _:
            print("Hello, Stranger")
greet("A")
#-> Hello, A
greet("B")
#-> Hello, B
greet("Victor")
#-> Hello, Victor
greet("Karina")
#-> Hello, Stranger

"""
Match Case Statement with OR Operator
Declaración de caso coincidente con el operador OR

"""

def num_check(x):
    match x:
        case 10 | 20 | 30: #Macthes 10, 20 or 30.
            print(f"Matched: {x}")
        case _:
            print("No match found")

num_check(10)
# ->Matched: 10
num_check(20)
# ->Matched: 20
num_check(50)
# -> No match found

"""
Match Case Statement with Python If Condition
Declaracion de caso coincidente con la condicion if de Python
"""

def num_check(x):
    match x:
        case 10 if x % 2 == 0: #match 10 only if it's even
            print("Matched 10 and it's even!")
        case 10:
            print("Matched 10, but it;s not even.")
        case _:
            print("No match found.")

num_check(10)
# -> Matched 10 and it's even!
num_check(18)
# -> No match found.

"""
Match Case Statement on Sequences
Declaracion de casos de coincidencia en secuencias
"""

def process (data):
    match data:
        case[x,y]:
            #A list with two elements
            print(f"Two-element list: {x}, {y}")
        case[x,y,z]:
            #A list with three elements
            print(f"Three-elements list: {x}, {y}, {z}")
        case[w,x,y,z]:
            #A list with three elements
            print(f"Four-elements list:{w}, {x}, {y}, {z}")
        case _:
            print("Unknown data format")
process([1,2])
# -> Two-element list: 1, 2

process([1,2,3])
# -> Two-element list: 1, 2, 3

process([1,2,3,4])
# -> Two-element list: 1, 2, 3, 4

process([1,2,3,4,5])
# -> Unknown data format.

"""
Match Case Statement on Mappings (Dictionaries)
"""
def person(person):
    match person:
        #Dictionary with name and age keys.
        case {"name": name, "age": age}:
            print(f"Name {name}, Age:{age}")
        #Dictionary with only name key
        case {"name":name}:
            print(f"Name: {name}")
        case _:
            print("Unknown format")

person({"name":"alice", "age":25})
# -> Name alice, Age:25

person({"name":"Bob"})
# Name: Bob

person({"City":"New York"})
# Unknown format


"""
Match Case Statement with Python Class.
Declaracion de caso coincidente con la clase de python.
"""
class Shape:
    pass

class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height

def check_shape(shape):
    match shape:

        # Match Circle and extract the radius
        case Circle(radius):
            print(f"circle radius {radius}.")

        # Match Rectangle and extract width and height
        case Rectangle(width, height):
            print(f"Rectangle width {width} and height {height}.")

        # Default case for any other object
        case _:
            print("This is an unknown shape.")

# Create objetcs of circle and rectangle
circle =  Circle(10)
rectangle = Rectangle(4, 6)

# Test with different shapes
check_shape (circle)
check_shape (rectangle)