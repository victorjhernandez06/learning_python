# Encontrar el nombre del Sistema Operativo SO, el nombre y la version de la plataforma.
import os
import platform

#importamoos os, y platform

print(os.name) #==> nos mostrara el nombre del sistema operativo.
# --> nt, lo que quiere decir que estamos en el sistema operativo windows
# --> posix, quiere decir que es linux

print(platform.system()) # nos muestra el nombre del sistema operativo.
# --> Windows

print(platform.release()) # el numero de la version.
# --> 11

