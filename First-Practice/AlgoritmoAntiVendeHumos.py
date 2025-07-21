def detectar_vende_humo(texto):
    palabras_clave = [
        "dinero fácil", "sin esfuerzo", "desde casa", "trabaja 1 hora",
        "hazte rico", "sin experiencia", "100% garantizado", "ingresos pasivos ya"
    ]
    contador = sum([1 for palabra in palabras_clave if palabra in texto.lower()])
    if contador >= 2:
        return True
    return False

ejemplo = "Gana dinero fácil desde casa con solo 1 hora al día y sin experiencia"
print(detectar_vende_humo(ejemplo))  # True
