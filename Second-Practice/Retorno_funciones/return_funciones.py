#Multiplicador
def multiplicador(factor):
    def funcion_interna(numero):
        return numero * factor
    return funcion_interna # Se retorna la funcion, pero coloca sin el parentesis para convertirla en funcion objeto.

multiplicar_por_2 = multiplicador(2)
multiplicar_por_5 = multiplicador(5)

print(multiplicar_por_2(3)) #yo aqui tengo que colocar un parametro, aqui siempre va a multiplicar por 2, el argumento que envie
print(multiplicar_por_5(4)) #yo aqui tengo que colocar un parametro, aqui siempre va a multiplicar por 5, el argumento que envie.