from empleado import Empleado
from Cliente import Cliente

def cargar():
    respuesta = input('van a agregar a un empleado? ')
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    dni = input("ingrese el dni: ")
    telefono = input("ingrese el telefono: ")

    if (respuesta == 'si'):
        salario = input('Ingresa el salario: ')
        emp = Empleado(nombre, apellido, dni, telefono, int(salario))
        personas.append(emp)
    else:
        tipo = input('Ingresa el tipo de cliente: ')
        cliente = Cliente(nombre, apellido, dni, telefono, tipo)
        personas.append(cliente)

personas = []
cargar()
cargar()

for persona in personas:
    print (persona)