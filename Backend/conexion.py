import mysql.connector
from mysql.connector import Error
#Conexion con MySQL#
class ConexionDB:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='Empresa 1',

            )
            print("La conexión a la base de datos fue exitosa")

        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def cerrar_conexion(self):
        if self.connection.is_connected():
            self.connection.close()
            print("La conexión a la base de datos ha sido cerrada")



