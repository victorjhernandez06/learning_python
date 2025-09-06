# Consultar las variables de entorno del sistema
import os
#conocer la ruta del usuario actual.

print(os.environ['USERPROFILE'])
print('*'*50)
print(os.environ['PATH'])
print('*'*50)
print(os.environ.get('HOME', 'No existe la variable HOME'))
print('*'*50)
# podriamos tener todas las variables de entorno definidas.
print(os.environ)