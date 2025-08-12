import mysql.connector

class Cities:
    def __init__(self):
        self.cnn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "bdEjemploPy"
        )

    def __str__(self):
        datos = self.consulta_db()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_db(self):
        cur = self.cnn.cursor()  # El cursor es el objeto que permite ejecutar el script de sql
        sql = "SELECT * FROM countries"
        cur.execute(sql)  # esta consulta la obtenemos del sql
        data1 = cur.fetchall()
        cur.close()
        return data1

    def insert_city(self, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO countries(ISO3, CountryName, Capital, CurrencyCode)
        VALUES('{}','{}','{}','{}')'''.format(ISO3, CountryName, Capital,CurrencyCode)
        cur.execute(sql)
        n = cur.rowcount # con cur.rowcount, lo que hacemos es contar las filas y se la asignamos a la variable n.
        self.cnn.commit() #hacemos un commit para que se lleve a cabo
        cur.close()
        return n

    def delete_city(self, id):
        cur = self.cnn.cursor()
        sql = "DELETE FROM countries WHERE id = {}".format(id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def update_city(self, id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql = """UPDATE countries SET 
            ISO3='{}',
            CountryName='{}',
            Capital='{}', 
            CurrencyCode='{}'
            WHERE id = {} """.format(ISO3, CountryName, Capital, CurrencyCode, id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

