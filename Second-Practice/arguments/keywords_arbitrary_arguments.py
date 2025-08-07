# ** Kwargs
def imprimir_info(**info):
   for clave, valor in info.items():
       print(f"{clave}: '{valor}'")

# nombre: 'victor'
# edad: '42'
# ciudad: 'Cojedes'

imprimir_info(nombre="victor", edad=42, ciudad="Cojedes")