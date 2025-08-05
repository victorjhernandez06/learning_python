# Calcular el valor futuro para una cantidad, interes y numero de anos especificos.

# vf = va (1 + i)

def valor_futuro(vp, i, n):
    return vp * (1 + i) ** n

valor_presente  = 10000
interes = 3.5
periodos = 7

print(valor_futuro(valor_presente,interes/100, periodos))