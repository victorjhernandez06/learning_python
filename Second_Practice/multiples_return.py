def function_conditional(valor):
    if valor > 0: 
        return "Positivo"
    elif valor < 0:
        return "Negativo"
    else:
        return "Cero"
    
    
resultado_conditional = function_conditional(-7)
print(resultado_conditional)

resultado_conditional2 = function_conditional(1)
print(resultado_conditional2)

print(function_conditional(0))