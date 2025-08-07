class Coche():

    def __init__(self):
        self.__largoChasis = 250 #Al colocar los dos guiones antes de la variable, le estoy encapsulando.
        self.__anchoChasis = 120 #Al colocar los dos guiones antes de la variable, le estoy encapsulando.
        self.__ruedas = 4 #Al colocar los dos guiones antes de la variable, le estoy encapsulando.
        self.__enmarcha = False #Al colocar los dos guiones antes de la variable, le estoy encapsulando.

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            return "el coche esta en marcha"
        else:
            return "El coche esta detenido"


    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un anche de:", self.__anchoChasis, "y un largo de ", self.__largoChasis)



miCoche = Coche()
print(miCoche.arrancar(True)) #si no llamamos este metodo, el coche no arranca.
print(miCoche.estado())

# el coche esta en marcha
# El coche tiene 4 ruedas. Un anche de: 120 y un largo de  250
# None

print("-----------------Nuevo coche-------------")

miCoche2 = Coche()
print(miCoche.arrancar(False) )#si no llamamos este metodo, el coche no arranca.
miCoche2.__ruedas = 2 # si la variable esta encapsulada, no puedo modificarle
print(miCoche2.estado())

# El coche esta detenido
# El coche tiene 4 ruedas. Un anche de: 120 y un largo de  250
# None


print("----------------- El Perro -------------")
class Dog:
    species =  "Canine" #class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 =  Dog("Draco", 2)
print(dog1.name)
print(dog1.age)
print(dog1.species)

print("----------------- El Perro 2 -------------")
dog2 = Dog("Chispa", 4)
print(dog2.name, dog2.age, dog2.species)
print(Dog.species)

# -> Drago
# -> 2

#Python objects
#An objects is an instance of a Class.
# Represent by methods of an object and reflects the response of un object to other objects

print("----------------- Constructor -------------")
"""
__init__ Method
"""

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Minino", 3)

print("The Cat's name is:" ,cat1.name, "and he is:", cat1.age," years old" )
#-> The Cat name is: Minino and have: 3  years old


print("----------------- Class and Instance Variables-------------")

class Animal:
    species  = "Canine"

    def __init__(self, name, age):
        self.age = age
        self.name = name

#create objects
animal1 =  Animal("Robin", 2)
animal2 =  Animal("emperator",3)

print(animal2.name)
print(animal1.name)
# emperator
# Robin
#modify class variable
print(animal1.species)
animal2.species =  "Feline"
print(animal2.species)

# Canine
# Feline


#modify instance variable
animal1.name="batman"
print(animal1.name)

# batman


print("-----------------Python inheritance / Herencia de Python -------------")

class Zoo:
    def __init__(self,name):
        self.name = name

    def display_name(self):
        print(f"Dog's name : {self.name}")

#single Inheritance
class Labrador(Zoo):
    def sound(self):
        print("EL perro ladra.")

 #multilevel inheritance
class GuideDog(Labrador):
    def guide (self):
        print(f"{self.name} Guides the way")

#multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly")

#Multiple Inheritance
class GoldenRetriever(Dog, Friendly):
    def sound(self):
        print("Golden retriever Barks")

#Example usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog=GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


