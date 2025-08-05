# Crea una jerarquia de herencia basica

# Persona <-- Estudiante

class Persona:
    def __init__(self, documento, nombre, apellido, edad, email):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

class Estudiante(Persona):
    def __init__(self, documento, nombre, apellido,  edad, email, carnet, carrera ):
        super().__init__(documento, nombre, apellido,  edad, email)
        self.carnet = carnet
        self.carrera = carrera


victor = Estudiante ('123', 'Victor', 'Hernandez', 43,'e@mail.com','unellez', 'Ingenieria')
print(isinstance(victor, Estudiante)) #--> True
print(isinstance(victor, Persona))

dni = int(input("Ingrese un numero: "))
nme = input('Indica tu nombre: ')
ln = input('ingresa tu apellido: ')
age = int(input('Indica tu edad: '))
correo = input('indica tu email: ')
school = input('lugar de estudios: ')
carrer = input('Que carrera has estudiado: ')

p1 = Estudiante(dni, nme, ln, age, correo, school,carrer)
p2 = Estudiante(123,'Victor','Hernandez', 42,'vict@gmail.com', "Unellez-ven", 'Agroindustria')
print(f'el estudiante se llama {p1.nombre} {p1.apellido}, numero de documento: {p1.documento}, email: {p1.email}, el cual proviene de la casa de estudios: "{p1.carnet}" y es "{p1.carrera}"')
print(p2.nombre)

