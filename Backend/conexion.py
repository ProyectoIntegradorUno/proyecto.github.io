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

import mysql.connector
from mysql.connector import Error




class crudusuarios:
    def __init__(self):
        self.conexion_db =  ConexionDB()

    def crear_usuario(self, cuil, nombre, apellido, rol, password):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("INSERT INTO usuarios (cuil, nombre, apellido, rol, password) VALUES (%s, %s, %s, %s, %s)", (cuil, nombre, apellido, rol, password))
            self.conexion_db.connection.commit()
            print("Usuario creado exitosamente")

        except Error as ex:
            print("Error al crear usuario: {0}".format(ex))

    def leer_usuario(self, cuil):
        try:
            cursor = self.conexion_db.connection.cursor()
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
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, rol = %s, password = %s WHERE cuil = %s", (nuevo_nombre, nuevo_apellido, nuevo_rol, nueva_password, cuil))
            self.conexion_db.connection.commit()
            print("Usuario actualizado exitosamente")

        except Error as ex:
            print("Error al actualizar usuario: {0}".format(ex))

    def eliminar_usuario(self, cuil):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("DELETE FROM usuarios WHERE cuil = %s", (cuil,))
            self.conexion_db.connection.commit()
            print("Usuario eliminado exitosamente")

        except Error as ex:
            print("Error al eliminar usuario: {0}".format(ex))

    
import mysql.connector
from mysql.connector import Error




class CrudFacturas:
    def __init__(self):
        self.conexion_db =  ConexionDB()

    def crear_factura(self, fecha, modo_de_pago, cuit):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("INSERT INTO facturas (fecha, modo_de_pago, cuit) VALUES (%s, %s, %s)", (fecha, modo_de_pago, cuit))
            self.conexion_db.connection.commit()
            print("Factura creada exitosamente")

        except Error as ex:
            print("Error al crear factura: {0}".format(ex))

    def leer_factura(self, idfactura):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("SELECT * FROM facturas WHERE idfactura = %s", (idfactura,))
            factura = cursor.fetchone()
            if factura:
                print("Factura encontrada:")
                print(factura)
            else:
                print("Factura no encontrada")

        except Error as ex:
            print("Error al leer factura: {0}".format(ex))

    def actualizar_factura(self, idfactura, nueva_fecha, nuevo_modo_de_pago, nuevo_cuit):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("UPDATE facturas SET fecha = %s, modo_de_pago = %s, cuit = %s WHERE idfactura = %s", (nueva_fecha, nuevo_modo_de_pago, nuevo_cuit, idfactura))
            self.conexion_db.connection.commit()
            print("Factura actualizada exitosamente")

        except Error as ex:
            print("Error al actualizar factura: {0}".format(ex))

    def eliminar_factura(self, idfactura):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("DELETE FROM facturas WHERE idfactura = %s", (idfactura,))
            self.conexion_db.connection.commit()
            print("Factura eliminada exitosamente")

        except Error as ex:
            print("Error al eliminar factura: {0}".format(ex))

import mysql.connector
from mysql.connector import Error




class CrudItemsFactura:
    def __init__(self):
        self.conexion_db =  ConexionDB()

    def crear_item_factura(self, cantidad, precio, idproducto, idfactura):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("INSERT INTO itemsfactura (cantidad, precio, idproducto, idfactura) VALUES (%s, %s, %s, %s)", (cantidad, precio, idproducto, idfactura))
            self.conexion_db.connection.commit()
            print("Item de factura creado exitosamente")

        except Error as ex:
            print("Error al crear item de factura: {0}".format(ex))

    def leer_item_factura(self, iditems):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("SELECT * FROM itemsfactura WHERE iditems = %s", (iditems,))
            item = cursor.fetchone()
            if item:
                print("Item de factura encontrado:")
                print(item)
            else:
                print("Item de factura no encontrado")

        except Error as ex:
            print("Error al leer item de factura: {0}".format(ex))

    def actualizar_item_factura(self, iditems, nueva_cantidad, nuevo_precio, nuevo_idproducto, nuevo_idfactura):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("UPDATE itemsfactura SET cantidad = %s, precio = %s, idproducto = %s, idfactura = %s WHERE iditems = %s", (nueva_cantidad, nuevo_precio, nuevo_idproducto, nuevo_idfactura, iditems))
            self.conexion_db.connection.commit()
            print("Item de factura actualizado exitosamente")

        except Error as ex:
            print("Error al actualizar item de factura: {0}".format(ex))

    def eliminar_item_factura(self, iditems):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("DELETE FROM itemsfactura WHERE iditems = %s", (iditems,))
            self.conexion_db.connection.commit()
            print("Item de factura eliminado exitosamente")

        except Error as ex:
            print("Error al eliminar item de factura: {0}".format(ex))

    class crudProductos:
    def init(self):
        self.conexion_db = ConexionDB() 

    def crear_producto(self, descripcion, unidad, imagen, precio, tipo):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("INSERT INTO productos (descripcion, unidad, imagen, precio, tipo) VALUES (%s, %s, %s, %s, %s)", (descripcion, unidad, imagen, precio, tipo))
            self.conexion_db.connection.commit()
            print("Producto creado exitosamente")

        except Error as ex:
            print("Error al crear producto: {0}".format(ex))

    def leer_producto(self, idproductos):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("SELECT * FROM productos WHERE idproductos = %s", (idproductos,))
            producto = cursor.fetchone()
            if producto:
                print("Producto encontrado:")
                print(producto)
            else:
                print("Producto no encontrado")

        except Error as ex:
            print("Error al leer producto: {0}".format(ex))

    def actualizar_producto(self, idproductos, nueva_descripcion, nueva_unidad, nueva_imagen, nuevo_precio, nuevo_tipo):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("UPDATE productos SET descripcion = %s, unidad = %s, imagen = %s, precio = %s, tipo = %s WHERE idproductos = %s", (nueva_descripcion, nueva_unidad, nueva_imagen, nuevo_precio, nuevo_tipo, idproductos))
            self.conexion_db.connection.commit()
            print("Producto actualizado exitosamente")

        except Error as ex:
            print("Error al actualizar producto: {0}".format(ex))

    def eliminar_producto(self, idproductos):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("DELETE FROM productos WHERE idproductos = %s", (idproductos,))
            self.conexion_db.connection.commit()
            print("Producto eliminado exitosamente")

        except Error as ex:
            print("Error al eliminar producto: {0}".format(ex))



import mysql.connector
from mysql.connector import Error




class crudTipoProductos:
    def init(self):
        self.conexion_db = ConexionDB()  

    def crear_tipo_producto(self, descripcion):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("INSERT INTO tipoProductos (descripcion) VALUES (%s)", (descripcion,))
            self.conexion_db.connection.commit()
            print("Tipo de producto creado exitosamente")

        except Error as ex:
            print("Error al crear tipo de producto: {0}".format(ex))

    def leer_tipo_producto(self, idtiproductos):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("SELECT * FROM tipoProductos WHERE idtiproductos = %s", (idtiproductos,))
            tipo_producto = cursor.fetchone()
            if tipo_producto:
                print("Tipo de producto encontrado:")
                print(tipo_producto)
            else:
                print("Tipo de producto no encontrado")

        except Error as ex:
            print("Error al leer tipo de producto: {0}".format(ex))

    def actualizar_tipo_producto(self, idtiproductos, nueva_descripcion):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("UPDATE tipoProductos SET descripcion = %s WHERE idtiproductos = %s", (nueva_descripcion, idtiproductos))
            self.conexion_db.connection.commit()
            print("Tipo de producto actualizado exitosamente")

        except Error as ex:
            print("Error al actualizar tipo de producto: {0}".format(ex))

    def eliminar_tipo_producto(self, idtiproductos):
        try:
            cursor = self.conexion_db.connection.cursor()
            cursor.execute("DELETE FROM tipoProductos WHERE idtiproductos = %s", (idtiproductos,))
            self.conexion_db.connection.commit()
            print("Tipo de producto eliminado exitosamente")

        except Error as ex:
            print("Error al eliminar tipo de producto: {0}".format(ex))