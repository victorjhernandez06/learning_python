# Obtener la fecha y hora actuales del sistema
import datetime
ahora = datetime.datetime.now()
print(ahora) #--> 2025-07-30 00:12:50.345009

print(type(ahora)) #--> <class 'datetime.datetime'>

print(ahora.strftime('%d/%m/%Y %H:%M:%S')) # --> 30/07/2025 00:15:24
