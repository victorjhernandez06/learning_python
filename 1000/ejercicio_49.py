# Mostrar los archivos de un directorio especifico
from os import listdir
from os.path import isfile, join


ruta = r'G:\Bitacora'
ruta2 = r'F:\Python25\LearningPython'

def listar_directorio(ruta):
    """Lista el contenido de archivos de un directorio espeficico"""
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]
    return archivos

listar_archivos = listar_directorio(ruta)


print(listar_archivos) #==> imprime la lista creada anteriormente.

print(len(listar_archivos)) #58 files.