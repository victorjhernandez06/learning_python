num_years = 1.5
num_camels = 23

#--> con esta linea leemos el archivo.txt
# La funcion toma una linea y compruea si pertenece a una de las lneas especiales. Utiliza el metodo startswith, que comprueba si una cadena comienza con una secuencia de caracteres dada.
reader = open('pg345.txt') 
def is_special_line(line):  
    return line.startswith('*** ')


#podemos utilizar e for para recorrer las lineas del archivo e imprimir solo las lineas especiales 
for line in reader:
    if is_special_line(line):
        print(line.strip())