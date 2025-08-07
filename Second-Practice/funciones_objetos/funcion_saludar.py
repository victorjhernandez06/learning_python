def saludar(nombre):
    return f"Hola, {nombre}"


mi_funcion = saludar  # Al no colocar la funcion con el parentesis, queda como funcion objeto.
# Aquí creamos una referencia a la funcion, la cual la estamos tratando como objeto, para ello no colocamos el parentesis.

mensaje = mi_funcion("victor")
print(mensaje)