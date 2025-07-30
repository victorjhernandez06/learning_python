# Imprimir el calendario para un year an month especifico
import calendar

year = int(input('Escriba el year: '))
mes = int(input('Escriba el mes: '))

print(calendar.month(year, mes))
#      March 2023
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31