# Crear una clase para representar los datos de una persona

class Persona:
    def __ini__(self,edad,nombre,correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

        def __str__(self):
            return 'Nombre: {}\nEdad: {}\cCorreo: {}'