class Perro():
    """Modelo sencillo"""
    def __init__(self, nombre, edad):
        """Inicializacion atributos de nombre y edad"""
        self.nombre = nombre
        self.edad = edad

    def sentarse(self):
        '''Simula sentarse'''
        print(f"{self.nombre} se ha sentado.. ")

    def rodar(self):
        """Simula rodar en el piso"""
        print(f"{self.nombre} rodo en el piso")

mi_perro = Perro('Willi',6)

print(f"mi perro se llama {mi_perro.nombre}.")
print("mi perro se llama " + mi_perro.nombre + ".")
print(f"Mi perro tiene {mi_perro.edad} a#0s de edad.")
print("Mi perro tiene " + str(mi_perro.edad) + " a#os de edad.")

mi_perro.sentarse()
mi_perro.rodar()

