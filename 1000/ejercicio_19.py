#comprobar si una cadena termina con la extension py, sino es asi debemos agregarlo.

# main.py
# modulo -> modulo.py

def validar_nombre_archivo(nombre_archivo):
    """"
    Valida si un nombre de archivo tiene la extension .py
    Si el archivo no tiene la extension, la agrega.
    """
    if len(nombre_archivo) >= 3 and nombre_archivo[-3:] == '.py':
        return nombre_archivo

    return nombre_archivo +'.py'

print(validar_nombre_archivo('main.py'))
print(validar_nombre_archivo('modulo'))