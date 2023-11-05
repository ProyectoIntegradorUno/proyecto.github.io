from conexion import *

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


class CrudUsuarios:
    def _init_(self):
        self.conexion_db = self.conectar_db()

    def crear_usuario(self, cuil, nombre, apellido, rol, password):
        try:
            cursor = self.conexion_db.cursor()
            cursor.execute("INSERT INTO usuarios (cuil, nombre, apellido, rol, password) VALUES (%s, %s, %s, %s, %s)", (cuil, nombre, apellido, rol, password))
            self.conexion_db.commit()
            print("Usuario creado exitosamente")

        except Error as ex:
            print("Error al crear usuario: {0}".format(ex))

    def leer_usuario(self, cuil):
        try:
            cursor = self.conexion_db.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE cuil = %s", (cuil,))
            usuario = cursor.fetchone()
            if usuario:
                print("Usuario encontrado:")
                print(usuario)
            else:
                print("Usuario no encontrado")

        except Error as ex:
            print("Error al leer usuario: {0}".format(ex))

    def actualizar_usuario(self, cuil, nuevo_nombre, nuevo_apellido, nuevo_rol, nueva_password):
        try:
            cursor = self.conexion_db.cursor()
            cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, rol = %s, password = %s WHERE cuil = %s", (nuevo_nombre, nuevo_apellido, nuevo_rol, nueva_password, cuil))
            self.conexion_db.commit()
            print("Usuario actualizado exitosamente")

        except Error as ex:
            print("Error al actualizar usuario: {0}".format(ex))

    def eliminar_usuario(self, cuil):
        try:
            cursor = self.conexion_db.cursor()
            cursor.execute("DELETE FROM usuarios WHERE cuil = %s", (cuil,))
            self.conexion_db.commit()

        except Error as ex:
            print("Error al eliminar usuario: {0}".format(ex))

    def cerrar_conexion(self):
        if self.conexion_db.is_connected():
            self.conexion_db.close()
            print("Conexión a la base de datos cerrada.")

##