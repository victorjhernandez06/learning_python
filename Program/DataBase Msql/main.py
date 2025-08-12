import mysql.connector

cnn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "world"
)
print(cnn)


