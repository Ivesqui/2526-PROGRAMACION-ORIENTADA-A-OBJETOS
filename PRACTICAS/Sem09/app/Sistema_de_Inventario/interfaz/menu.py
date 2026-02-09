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

        # AÑADIR PRODUCTO
        if opcion == "1":
            sku = input("SKU: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(sku, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        # ELIMINAR PRODUCTO POR SKU
        elif opcion == "2":
            sku = input("SKU del producto a eliminar: ")
            inventario.eliminar_producto(sku)

        # ACTUALIZAR PRODUCTO POR SKU
        elif opcion == "3":
            sku = input("SKU del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            inventario.actualizar_producto(
                sku,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        # BUSCAR PRODUCTO (por nombre o SKU)
        elif opcion == "4":
            texto = input("Ingrese nombre o SKU a buscar: ")
            inventario.buscar_producto(texto)

        # LISTAR INVENTARIO
        elif opcion == "5":
            inventario.listar_productos()

        # SALIR
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente")

