from cruds import *
import sys

def main_menu():
    while True:
        print("Menú Principal:")
        print("1. Gestionar Clientes")
        print("2. Gestionar Usuarios")
        print("3. Gestionar Facturas")
        print("4. Gestionar Items de Factura")
        print("5. Gestionar Productos")
        print("6. Gestionar Tipos de Productos")
        print("7. Gestionar Roles")
        print("8. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            gestionar_clientes()
        
        elif choice == '2':
            gestionar_usuarios()

        elif choice == '3':
            gestionar_factura()
        
        elif choice == '4':
            gestionar_item_factura()
            
      
            print("Saliendo del programa.")
            sys.exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_clientes():
    cliente_crud = CrudClientes()
    while True:
        print("Gestión de Clientes:")
        print("1. Crear Cliente")
        print("2. Leer Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            cuit = input("Cuit: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            mail = input("Mail: ")
            domicilio_fiscal = input("Domicilio Fiscal: ")
            domicilio_de_entrega = input("Domicilio de Entrega: ")
            telefono = input("Teléfono: ")
            password = input("Password: ")
            verificado = input("Verificado: ")
            cliente_crud.crear_cliente(cuit, nombre, apellido, mail, domicilio_fiscal, domicilio_de_entrega, telefono, password, verificado)
        elif choice == '2':
            cuit = input("Cuit del Cliente a Leer: ")
            cliente_crud.leer_cliente(cuit)
        elif choice == '3':
            cuit = input("Cuit del Cliente a Actualizar: ")
            nuevo_nombre = input("Nuevo Nombre: ")
            nuevo_apellido = input("Nuevo Apellido: ")
            nuevo_mail = input("Nuevo Mail: ")
            cliente_crud.actualizar_cliente(cuit, nuevo_nombre, nuevo_apellido, nuevo_mail)
        elif choice == '4':
            cuit = input("Cuit del Cliente a Eliminar: ")
            cliente_crud.eliminar_cliente(cuit)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_usuarios():
    usuario_crud = crudusuarios()
    while True:
        print("Gestión de Usuarios:")
        print("1. Crear Usuario")
        print("2. Leer Usuarios")
        print("3. Actualizar Usuarios")
        print("4. Eliminar Usuarios")
        print("5. Volver al Menú Principal")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            cuit = input("Cuit: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            rol = input("Rol: ")
            password = input("Password: ")
            usuario_crud.crear_usuario(cuit, nombre, apellido, rol, password,)
        elif choice == '2':
            cuit = input("Cuit del Usuario a Leer: ")
            usuario_crud.leer_usuario(cuit)
        elif choice == '3':
            cuit = input("Cuit del Usuario a Actualizar: ")
            nuevo_nombre = input("Nuevo Nombre: ")
            nuevo_apellido = input("Nuevo Apellido: ")
            nuevo_mail = input("Nuevo Mail: ")
            nuevo_rol = input("Nuevo Rol")
            usuario_crud.actualizar_usuario(cuit, nuevo_nombre, nuevo_apellido, nuevo_mail, nuevo_rol)
        elif choice == '4':
            cuit = input("Cuit del Usuario a Eliminar: ")
            usuario_crud.eliminar_usuario(cuit)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_factura():
    facturas_crud = CrudFacturas()
    while True:
        print("Creacion De Factura:")
        print("1. Crear Factura")
        print("2. Leer Factura")
        print("3. Actualizar Factura")
        print("4. Eliminar Factura")
        print("5. Volver al Menú Principal")
        choice = input("Selecciona una opción: ")
        
        if choice == '1':
            fecha = input("Fecha: ")
            modo_de_pago = input("Modo de pago: ")
            cuit = input("Cuit: ")
            facturas_crud.crear_factura(cuit, fecha, modo_de_pago)
        elif choice == '2':
            cuit = input("Cuit de la Factura a Leer: ")
            facturas_crud.leer_factura(cuit)
        elif choice == '3':
            cuit = input("Cuit de la Factura a Actualizar: ")
            nuevo_nombre = input("Nuevo Nombre: ")
            nuevo_apellido = input("Nuevo Apellido: ")
            nuevo_mail = input("Nuevo Mail: ")
            nuevo_rol = input("Nuevo Rol")
            facturas_crud.actualizar_factura(cuit, nuevo_nombre, nuevo_apellido, nuevo_mail, nuevo_rol)
        elif choice == '4':
            cuit = input("Cuit de la Factura a Eliminar: ")
            facturas_crud.eliminar_factura(cuit)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    
def gestionar_item_factura():
    item_crud = CrudItemsFactura()
    while True:
        print("Creacion De Item de Factura:")
        print("1. Crear Item de Factura")
        print("2. Leer Item de Factura")
        print("3. Actualizar Item de Facturacion")
        print("4. Eliminar Item de facturacion")
        print("5. Volver al Menú Principal")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            cantidad = input("Cantidad: ")
            Precio = input("Precio: ")
            idproducto = input("Idproducto: ")
            idFactura = input("IdFactura:")
            item_crud.crear_item_factura(cantidad, Precio, idproducto, idFactura)
        elif choice == '2':
            idFactura = input("ID de la Factura a Leer: ")
            item_crud.leer_item_factura(idFactura)
        elif choice == '3':
            idFactura = input("ID de la Factura a Actualizar: ")
            nueva_cantidad = input("Nuevo Nombre: ")
            nuevo_precio = input("Nuevo Apellido: ")
            nuevo_idproducto = input("Nuevo Mail: ")
            nuevo_idFactura = input("Nuevo Rol")
            item_crud.actualizar_item_factura(idFactura, nueva_cantidad, nuevo_idproducto, nuevo_precio, nuevo_idFactura)
        elif choice == '4':
            idFactura = input("ID de la Factura a Eliminar: ")
            item_crud.eliminar_item_factura(idFactura)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            
def gestionar_Productos():
    Productos_crud = crudProductos
    while True:
        print("Creacion Productos:")
        print("1. Crear Producto")
        print("2. Leer Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver al Menú Principal")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            idproductos = input ("ID del producto")
            unidad = input("Unidades: ")
            descripcion = input("Descripcion: ")
            imagen = input("Inserte imagen:")
            precio = input("Precio")
            tipo = input("Tipo de producto")
            Productos_crud.crear_producto(unidad, descripcion, imagen, precio, tipo, idproductos)
        elif choice == '2':
            idproductos = input("ID del Producto a leer: ")
            Productos_crud.leer_producto(idproductos)
        elif choice == '3':
            idproductos = input("ID de el Producto a Actualizar: ")
            nueva_descripcion = input("Nueva Descripcion: ")
            nueva_unidad = input("Nueva Unidad: ")
            nuevo_tipo = input("Nuevo Tipo: ")
            nueva_imagen = input("Nueva imagen")
            nuevo_precio = input()
            Productos_crud.actualizar_producto(idproductos, nueva_descripcion, nueva_unidad, nuevo_tipo, nueva_imagen, nuevo_precio)
        elif choice == '4':
            idproductos = input("ID de el Producto a Eliminar: ")
            Productos_crud.eliminar_producto(idproductos)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    


if __name__ == "__main__":
    main_menu()