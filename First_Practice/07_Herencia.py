#Herencia Simple
#Crear una clase, propiedades y metodos.

#clase padre
class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"{self.nombre} es de nacionalidad {self.nacionalidad}")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")



###___HERENCIA SIMPLE____
#El pass, es para llamar una funcion o metodo y no hacer nada.
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, profesion, reside):
        super().__init__(nombre, edad, nacionalidad)
        self.profesion = profesion
        self.reside = reside

estudiante = Estudiante ("Victor",43,"Venezolana (ve)","programador","United State")
estudiante_2 = Estudiante ("karina",42,"Venezolana (ve)","Ingeniera", "Venezuela")

print(f"{estudiante.nombre} tiene {estudiante.edad} años de edad y vive actualmente en {estudiante.reside}")
print(f"{estudiante_2.nombre} tiene {estudiante_2.edad} años de edad y vive actualmente en {estudiante_2.reside}")

estudiante.hablar()
estudiante_2.hablar()

###___HERENCIA MULTIPLE____
#Ojo en esta no se coloca el super().__init__ para llamar a la clase padre, porque en esta,
#hemos indicado que tenemos 2 padres: Persona y Artista.
class EmpleadoArtista(Persona, Artista):
    def __init__(self,nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def mostrar_habilidad(self):
        print("no tengo jaja")

    # Un ejemplo con super(), aqui se llama al método de la clase padre
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'

    #un ejemplo con self, aqui se llama al método que esta interno en la clase.
    def presentarse_repeat (self):
        return f'{self.mostrar_habilidad()}'


##COMO SABER DE DONDE VIENE UNA CLASE, COMO CONSEGUIR LA CLASE PADRE
#Usamos el metodo issubclass

herencia =  issubclass(EmpleadoArtista, Persona)
print (herencia)

# Como saber si es o no una instancia, para ellos usamos el isinstance()
instancia = isinstance(estudiante,EmpleadoArtista)
print(instancia)

instancia_dos = isinstance(estudiante,Estudiante)
print(instancia_dos)


