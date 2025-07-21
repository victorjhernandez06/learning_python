class Perro:
    #constructor
    def __init__(self, name, raza, color):
        self.size = None
        self.age = 0
        self.color = color
        self.raza = raza
        self.name = name

    #Metodos
    def ladrar(self):
        print(f"{self.name} is barking")

    def comer(self):
        print(f"{self.name} is eating")

    def jugar(self):
        print(f"{self.name} is playing")

    # setter && getter
    def cambiar_nombre(self,name):
        self.name = name
        print(f"El perro ahora se llama {name}")

    def set_edad(self,edad):
        self.edad = edad

    def birthday(self):
        self.edad += 1
        print(f"{self.name} is now {self.age} years old")



#instance
mi_perro = Perro("Tommy", "Dalmata","White && Black")
print("------Atributos -----")
print(mi_perro.name) #atributos
print(mi_perro.raza) #atributos
print(mi_perro.color) #atributos
print("------Metodos -----")
mi_perro.ladrar() #Metodo
mi_perro.comer()
mi_perro.jugar()
mi_perro.set_edad(1)
mi_perro.birthday()


mi_perro2 = Perro("Rex","Mierdero","Brown")
mi_perro2.set_edad(5)