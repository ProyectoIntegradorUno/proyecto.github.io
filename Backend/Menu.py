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

# Puedes agregar más funciones de gestión para otras entidades (Facturas, Items de Factura, Productos, Tipos de Productos, Roles) de manera similar.

if __name__ == "__main__":
    main_menu()