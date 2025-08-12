import mysql.connector

#Conecta la base de datos.
cnn = mysql.connector.connect(
    host = "localhost", #127.0.0.1, o IP del equipo remoto
    user = "root", #Nombre de usuario de la BD, con los permisos necesarios
    passwd = "", #Clave del usuario.
    database = "bdEjemploPy" #Nombre de la base de datos.
)


### -- SELECT -- ##
## Consulta los valores dentro de una base de datos
def consulta_bd():
    cur = cnn.cursor() #El cursor es el objeto que permite ejecutar el script de sql
    sql = "SELECT * FROM countries"
    cur.execute(sql) #esta consulta la obtenemos del sql
    data1 = cur.fetchall()
    cur.close()
    cnn.close()
    return data1

### -- INSERT -- ##
## Inserta datos dentro de la base de datos
def insert_city(ISO3, CountryName, Capital, CurrencyCode):
    cur = cnn.cursor()
    sql = '''INSERT INTO countries(ISO3, CountryName, Capital, CurrencyCode)
    VALUES('{}','{}','{}','{}')'''.format(ISO3, CountryName, Capital,CurrencyCode)
    cur.execute(sql)
    n = cur.rowcount # con cur.rowcount, lo que hacemos es contar las filas y se la asignamos a la variable n.
    cnn.commit() #hacemos un commit para que se lleve a cabo
    cur.close()
    return n

#llamamos a la funcion insert_city
# print(insert_city('ESP','Spain','Madrid', 'EUR'))

### -- DELETE -- ###
def delete_city(id):
    cur = cnn.cursor()
    sql = "DELETE FROM countries WHERE id = {}".format(id)
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n

# print(delete_city(11))

### -- UPDATE -- ##

def update_city(id,ISO3, CountryName, Capital, CurrencyCode):
    cur = cnn.cursor()
    sql = """UPDATE countries SET 
        ISO3='{}',
        CountryName='{}',
        Capital='{}', 
        CurrencyCode='{}'
        WHERE id = {} """.format(ISO3,CountryName,Capital,CurrencyCode, id)
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n

# print(update_city(9, 'EUA','Estados Unidos','Washington D.C','USD'))

### Esta instruccion solo consulta e imprime los valores de la base de datos
dat = consulta_bd()
if dat: #si la tabla tiene datos
    for fila in dat:
        print(fila)
else:
    print("No hay Datos!!")

# print(cnn)







