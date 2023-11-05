import mysql.connector
from mysql.connector import Error

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

cursor = conn.cursor()
cursor.execute("SELECT * FROM Productos")
for row in cursor.fetchall():
    print(row)

class CrudClientes:
    def __init__(self):
        self.conexion_db = ConexionDB()

    def crear_cliente(self, cuit, nombre, apellido, mail, domicilio_fiscal, domicilio_de_entrega, telefono, password, verificado):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("INSERT INTO Clientes (cuit, nombre, apellido, mail, domicilio_fiscal, domicilio_de_entrega, telefono, password, verificado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (cuit, nombre, apellido, mail, domicilio_fiscal, domicilio_de_entrega, telefono, password, verificado))
            self.conexion_db.connection.commit()
            print("Cliente creado exitosamente")

        except Error as ex:
            print("Error al crear cliente: {0}".format(ex))

    def leer_cliente(self, cuit):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("SELECT * FROM Clientes WHERE cuit = %s", (cuit,))
            cliente = cursor.fetchone()
            if cliente:
                print("Cliente encontrado:")
                print(cliente)
            else:
                print("Cliente no encontrado")

        except Error as ex:
            print("Error al leer cliente: {0}".format(ex))

    def actualizar_cliente(self, cuit, nuevo_nombre, nuevo_apellido, nuevo_mail):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("UPDATE Clientes SET nombre = %s, apellido = %s, mail = %s WHERE cuit = %s", (nuevo_nombre, nuevo_apellido, nuevo_mail, cuit))
            self.conexion_db.connection.commit()
            print("Cliente actualizado exitosamente")

        except Error as ex:
            print("Error al actualizar cliente: {0}".format(ex))

    def eliminar_cliente(self, cuit):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("DELETE FROM Clientes WHERE cuit = %s", (cuit,))
            self.conexion_db.connection.commit()
            print("Cliente eliminado exitosamente")

        except Error as ex:
            print("Error al eliminar cliente: {0}".format(ex))

