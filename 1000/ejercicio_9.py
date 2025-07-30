# Mostrar la fecha de un evento almacenada en una tupla
from calendar import month

fecha_evento = (2023, 9, 14)
print(type(fecha_evento)) # --> <class 'tuple'>

print(fecha_evento)
# (2023, 9, 14)

print('El evento programado sera para la fecha:', fecha_evento)
# El evento programado sera para la fecha: (2023, 9, 14)

print('El evento programado sera para la fecha: %i/%i/%i.'%fecha_evento) #--> El evento programado sera para la fecha, 2023/9/14

year, month, day = fecha_evento
print('El evento programado sera para la fecha: {}/{}/{}.'.format(year,month,day)) #--> El evento programado sera para la fecha: 2023/9/14

agnio, mes, dia = (2023, 9, 14)
print("El evento programado sera para la fecha: {}/{}/{}.".format(agnio,mes,dia)) #--> El evento programado sera para la fecha: 2023/9/14.
