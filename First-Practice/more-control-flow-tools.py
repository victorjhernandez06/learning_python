""" MORE CONTROL FLOW TOOLS """

# As well as the while statement just introduced, Python uses a few more that we will encounter in this part.

''' IF STATEMENTS'''

# Perhaps the most well-known statement.
# x = int(input("Please enter an integer: "))
x = 42
if x< 0:
    x = 0
    print('Negative change to zero')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('More')

#--> More

''' FOR STATEMENTS'''
# The for statement in python differs a bit form may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of number (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C) Python's for statement iterates over the items of any sequence(a list or a string), in the order that they appear in the sequence.

#Measure some strings
words = ['cat', 'window', 'defenestrate']
print(type(words)) #--> <class 'list'>
for w in words:
    print(w, len(w))
# cat 3
# window 6
# defenestrate 12

# Code that modifies a collection while iterating over that same collection can be tricky to get right. instead, its is usually more  straight-forward to loop over a copy of the collection or to create collection.

# Create a sample collection
users = {'Hans':'Active', 'Eleonore':'inactive','vjh':'active'}

#strategy: iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

#Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


''' THE RANGE() FUNCTION'''
# if you do need to iterate over a sequence of numbers, the build-in function range() come in handy. it generates arithmetic progressions:

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

a =  ['Mary','had','a', 'little','lamb']
for i in range(len(a)):
    print(i, a[i])
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

print(list(range(5,10))) # --> [5, 6, 7, 8, 9]
print(list(range(0,10,3))) #--> [0, 3, 6, 9]
print(list(range(-10,-100,-30))) #--> [-10, -40, -70]

# To iterate over the indices of a sequence, you can combine range() and len() as follows:

a = ['mary', 'had','a','little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 0 mary
# 1 had
# 2 a
# 3 little
# 4 lamb

# in most such cases, however, it is convenient to use the enumerate() function
# A strange thing happens if you print a range:

print(range(10))
#--> range(0, 10)
print(list(range(10)))
#--> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] Crea una lista desde el 0 hasta el 9

# in many way the object returned by range() behaves as if it a list, but in fact it isn't. It is an object which returns the successive items of the desired when you iterate over it, but it doesn't really make the list, thus saving space

print(sum(range(4)))
#--> 0+1+2+3 --> 6

'''BREAK AND CONTINUE STATEMENTS'''
# The break statement breaks out of the innermost enclosing for or while loop:

for n in range (2, 10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equals {x}*{n//x}")
            break
# 4 equals 2*2
# 6 equals 2*3
# 8 equals 2*4
# 9 equals 3*3

# the continue statement continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number{num}")
        continue
    print(f"Found an odd number{num}")
# Found an even number2
# Found an odd number3
# Found an even number4
# Found an odd number5
# Found an even number6
# Found an odd number7
# Found an even number8
# Found an odd number9

print('ELSE CLAUSES ON LOOPS')
'''ELSE CLAUSES ON LOOPS'''
# in a for or while loop the break statement may be paired with an else clause. If the loop finishes without executing the break, the else clause executes.
# in a for loop the else clause is executing after the loop finishes its final interaction, if no break occurred.
# in a while loop, it's executed after the loop's condition become false.
# In either kind of loop, the else clause is not executed if the loop was terminated by a break. Of course, other ways of ending the loop early such as a return or a raised exception, will also skip execution of the else clause.
# this is exemplified in the folllowing for loop, which searches for prime numbers:

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

'''PASS STATEMENTS'''
# the pass statement does nothing. It can be used when a statement is required syntactically, but the program requires no action.

# while True:
#     pass #--> Busy-wait for keyboard interrupt (ctrl+C)
#
# # this is commonly used creating minimal classes
# class MyEmptyClass:
#     pass
#
# # Another place pass can be used is as a place-holder for a function or conditional body when you are working on a new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored.
# def initlog(*args):
#     pass


"""MACTH STATEMENTS"""
# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. THis is superficially similar to a switch statement in C, JavaScript (and many other languages), but it's more similar to pattern matching in languages like Rust or Haskell. Only the first pattern matches gets executed and it can also extract components (sequences elementor object attributes) from vale into variables.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Note: The last block: the "variable name" _ acts as wildcard and never fails to match. if no case matches, none of the branches is executed.
# You can combine several literals in a single pattern using | ("or")

def https_error (status):
    match status:
        case 404 | 403 | 404:
            return "Not Allowed"

# Patterns can look like unpacking assignments, and can be used to bind variables:
# point is an (x, y) tuple
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")



# status = 400
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

# Note the last block: the "variable name" _ acts as a wilcard and never fails to match. If no case matches, none of the branches is executed.

# case 401 | 403 | 404:
#     return "Not allowed"

# patterns can look like unpacking assignments, and can be used to bind variable

# point is an (x, y) tuple
# match point:
#     case(0,0):
#         print('Origin')
#     case(0, y):
#         print(f"Y={y}")
#     case(x, 0):
#         print(f"X={x}")
#     case(x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

# Study that one carefully! the first pattern has two literals, and can be thought of as an extension of the literal pattern shown above. But the next two pattern combine a literal and a variable, and the variable binds a value from the subject(point). The fourth pattern captures two values, which makes it conceptually similar to the unpacking assignment (x,y) = point.

# If you are using classes to structure your data you can use the class name followed by an argument list resembling a constructor, but with the ability to capture attributes into variables:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def where_is(point):
        match point:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("somewhere else")
            case _:
                print("Not a point")

    def __str__(self):
        return f"Point({self.x}, {self.y})"

ejes = Point(0,0)
print(ejes) #--> Point(0, 0)
Point.where_is(ejes) #--> Origin

'''DEFINING FUNCTIONS'''

def fib(n):
    """Print a fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b =b, a+b
    print()
#now call the function we just defined:
fib(2000) #--> 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

f = fib
f(100) #--> 0 1 1 2 3 5 8 13 21 34 55 89
print(f)

fib(0)
print(fib(0)) #--> None

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f100 = fib2(200) #call it
print(f100) # --> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

