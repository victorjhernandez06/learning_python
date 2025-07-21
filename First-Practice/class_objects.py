

class Animal: #Clase Padre
    def __init__(self):
        self.edad = None #atributos clase padre
        self.especie = None #atributos clase padre
        self.pelaje = None #atributos clase padre

    def comer(self):
        print("El animal esta comiendo")   #metodos clase padre

    def reproducirse(self):
        print("El animal se reproduce")  #metodos clase padre

class Perro(Animal):
    def __init__(self, name, raza):
        super().__init__() # esto es para inicializar los atributos de la clase padre
        self.size = None
        self.raza = raza
        self.name = name

    #Metodos
    def ladrar(self):
        print(f"{self.name} is barking")

    def check_hambre(self, hambre):
        if hambre:
            self.comer()
        else:
            print(f"{self.name} no esta hambriento")

    def comer(self):
        print(f"")

    def jugar(self):
        print(f"{self.name} is playing")


draco = Perro("Draco","Rottweiler")
draco.reproducirse()

