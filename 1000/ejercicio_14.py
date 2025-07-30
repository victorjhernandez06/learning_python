#calcular la diferencia en dias de dos fechas.
from datetime import date
hoy = date(2025, 7, 30)
otra_fecha = date(2018,2,5)s

#calculamos la cantidad de dias y luego la imprimimos.
captains_log = otra_fecha - hoy

print(captains_log)
print(captains_log.days)



hoy1 = date.__doc__
print(hoy1)
