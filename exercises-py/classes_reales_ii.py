from empleado import Empleado
from Cliente import Cliente


emp = Empleado('Victor', 'Hernandez','1234','1818','2300')

cliente = Cliente('Karina', 'Jimenez','123','0258','VIP')

print(emp.apellido, emp.nombre)
print(cliente.apellido, cliente.nombre)