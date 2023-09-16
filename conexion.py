import mysql.connector
from mysql.connector import Error

class ConexionDB:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='929606lB',
                database='Empresa',
            )
            print("La conexión a la base de datos fue exitosa")

        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def cerrar_conexion(self):
        if self.connection.is_connected():
            self.connection.close()
            print("La conexión a la base de datos ha sido cerrada")

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

if __name__ == "__main__":
    crud_clientes = CrudClientes()
    
    # Ejemplo de creación de cliente
    crud_clientes.crear_cliente(
        cuit="12345678901",
        nombre="Juan",
        apellido="Perez",
        mail="juan@example.com",
        domicilio_fiscal="Calle Principal",
        domicilio_de_entrega="Calle Secundaria",
        telefono="555-555-5555",
        password="contraseña123",
        verificado=1
    )

    # Ejemplo de lectura de cliente
    crud_clientes.leer_cliente("12345678901")

    # Ejemplo de actualización de cliente
    crud_clientes.actualizar_cliente("12345678901", "Juanita", "Perez", "juanita@example.com")

    # Ejemplo de eliminación de cliente
    crud_clientes.eliminar_cliente("12345678901")

    # Cierra la conexión a la base de datos al finalizar
    crud_clientes.conexion_db.cerrar_conexion()
