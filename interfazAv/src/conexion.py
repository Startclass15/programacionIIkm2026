import mysql.connector

def conectar():
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="basedatosikm",
        port=3306
    )
    return conexion