from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    print("""
===== SISTEMA DE GESTIÓN DE INVENTARIOS =====
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto
5. Listar inventario
6. Salir
""")

def ejecutar_menu():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            idp = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(idp, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            idp = int(input("ID del producto: "))
            inventario.eliminar_producto(idp)

        elif opcion == "3":
            idp = int(input("ID del producto: "))
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            inventario.actualizar_producto(
                idp,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.listar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida, intente nuevamente")
