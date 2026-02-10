from modelos.producto import Producto
from servicios.inventario import Inventario
from reportes.reporte_excel import generar_excel_inventario

def mostrar_menu():
    """Muestra las opciones disponibles del sistema"""
    print("""
    ===== SISTEMA DE GESTIÓN DE INVENTARIOS =====
    1. Añadir producto
    2. Eliminar producto
    3. Actualizar producto
    4. Buscar producto
    5. Listar inventario
    6. Exportar inventario a Excel
    7. Salir
    """)


def ejecutar_menu():
    """
    Función principal del menú.
    Se encarga de interactuar con el usuario.
    """
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # AÑADIR PRODUCTO
        if opcion == "1":
            try:
                sku = input("SKU: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(sku, nombre, cantidad, precio)

                if inventario.agregar_producto(producto):
                    print("Producto agregado correctamente")
                else:
                    print("Error: SKU duplicado")

            except ValueError as e:
                print(f"Error: {e}")

        # ELIMINAR PRODUCTO
        elif opcion == "2":
            sku = input("SKU del producto a eliminar: ")

            if inventario.eliminar_producto(sku):
                print("Producto eliminado")
            else:
                print("Producto no encontrado")

        # ACTUALIZAR PRODUCTO
        elif opcion == "3":
            sku = input("SKU del producto: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            actualizado = inventario.actualizar_producto(
                sku,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

            if actualizado:
                print("Producto actualizado")
            else:
                print("Producto no encontrado")

        # BUSCAR PRODUCTO
        elif opcion == "4":
            texto = input("Ingrese nombre o SKU: ")
            productos = inventario.buscar_producto(texto)

            if productos:
                for p in productos:
                    print(
                        f"SKU: {p.get_sku()} | "
                        f"Nombre: {p.get_nombre()} | "
                        f"Cantidad: {p.get_cantidad()} | "
                        f"Precio: ${p.get_precio()}"
                    )
            else:
                print("No se encontraron productos")

        # LISTAR INVENTARIO
        elif opcion == "5":
            productos = inventario.listar_productos()

            if productos:
                for p in productos:
                    print(
                        f"SKU: {p.get_sku()} | "
                        f"Nombre: {p.get_nombre()} | "
                        f"Cantidad: {p.get_cantidad()} | "
                        f"Precio: ${p.get_precio()}"
                    )
            else:
                print("Inventario vacío")

        # GENERAR EXCEL

        elif opcion == "6":
            generar_excel_inventario()

        # SALIR
        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")
