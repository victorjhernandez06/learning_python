# Encontrar la ruta del script actual en ejecucion
import os

print(os.path.realpath(__file__))
# --> ruta absoluta --> F:\Python25\LearningPython\1000\ejercicio_46.py