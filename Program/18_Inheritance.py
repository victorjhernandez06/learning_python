"""Python inheritance"""
"""HERENCIA"""

# inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parents class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

"""Create a parent Class"""

# Any class can a parent class, so the syntax is the same as creating any another class.
# Example: Crear a class name Person, with firstname and lastname properties, mandd printname method:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person('Mathias','Hernandez')
x.printname()

"""Create a Child Class"""
# To create a class that inherits the functionality from another class, send the parent class a parameter when creating the child class.

# Example: Create a class name Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass

# Now the student class has the same properties and methods as the Person Class
x = Student('Adrian', 'Hernandez')
x.printname()
y = Student('Sofia','Hernandez')
y.printname()

"""Use the super() Function"""
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
# By using the super() fucntion, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

"""Add Properties"""
# Add a property called graduationyear to the Student class:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
# In the example below, the year 2019, should be a variable, and passed into the student class when creating student objects, To do so, add another parameter in the __init__() function:

# Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def printyear(self):
        print(x.graduationyear)
        
x = Student('Karina', 'Jimenez',2001)
x.printyear()

"""Add Methods"""
# Add a Method called welcome to the Student class:

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

p1 = Student('Adrian','Hernandez', 2026)
p1.welcome() #--> Welcome Adrian Hernandez to the class of 2026
p2 = Student('Mathias','Hernandez', 2031)
p3 = Student('Sofia', 'Hernandez', 2032)
p2.welcome() #--> Welcome Mathias Hernandez to the class of 2031
p3.welcome() #--> Welcome Sofia Hernandez to the class of 2032

# If you add a method in the child class with the same name, as a function in the parent class, the inheritance of the parent method will be overriden.
