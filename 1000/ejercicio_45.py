# Ejecutar un comando externo por medio de la funcion call.
from subprocess import call

print(call(['ping','google.com']))