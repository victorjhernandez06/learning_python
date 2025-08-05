# Localizar la ruta de los site-packages de la instancia de PythonFinalizationError.

# Buscar los directorios donde se instalan los modulos de Python
import site
from site import getsitepackages

print(site.getsitepackages())
# --> ['F:\\Python25\\LearningPython\\.venv', 'F:\\Python25\\LearningPython\\.venv\\Lib\\site-packages']



