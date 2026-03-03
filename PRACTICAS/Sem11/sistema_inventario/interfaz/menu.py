# ======================================================
# IMPORTACIONES
# ======================================================

from modelos.producto import Producto
from servicios.inventario import Inventario


# ======================================================
# FUNCIÓN PARA MOSTRAR EL MENÚ
# ======================================================
def mostrar_menu():
    """
    Muestra las opciones disponibles del sistema.
    """
    print("""
    ===== SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO =====
    1. Registrar producto
    2. Eliminar producto (eliminación física)
    3. Actualizar stock / precios
    4. Buscar producto por nombre
    5. Listar todos los productos
    6. Salir
    """)


# ======================================================
# FUNCIÓN PRINCIPAL DEL MENÚ
# ======================================================
def ejecutar_menu():
    """
    Controla el flujo principal del sistema.
    Permite al usuario interactuar con el inventario.
    """

    # Se crea la instancia del inventario
    # Automáticamente carga desde inventario.json
    inventario = Inventario()

    # Bucle principal del programa
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        # ======================================================
        # 1. REGISTRAR PRODUCTO
        # ======================================================
        if opcion == "1":
            try:
                sku = input("SKU: ").strip()
                nombre = input("Nombre del producto: ").strip()
                categoria = input("Categoría: ").strip()
                unidad = input("Unidad (pieza, caja, kg, etc): ").strip()
                precio_compra = float(input("Precio de compra: "))
                precio_venta = float(input("Precio de venta: "))
                stock = int(input("Stock inicial: "))
                stock_minimo = int(input("Stock mínimo: "))

                # Se crea el objeto Producto
                producto = Producto(
                    sku=sku,
                    nombre_producto=nombre,
                    categoria=categoria,
                    unidad=unidad,
                    precio_compra=precio_compra,
                    precio_venta=precio_venta,
                    stock_actual=stock,
                    stock_minimo=stock_minimo
                )

                # Se intenta agregar al inventario
                if inventario.agregar_producto(producto):
                    print("Producto registrado correctamente.")
                else:
                    print("Error: El SKU ya existe.")

            except ValueError as e:
                print("Error en los datos ingresados:", e)

        # ======================================================
        # 2. ELIMINAR PRODUCTO (FÍSICAMENTE)
        # ======================================================
        elif opcion == "2":
            sku = input("Ingrese el SKU del producto a eliminar: ").strip()

            if inventario.eliminar_producto(sku):
                print("Producto eliminado correctamente.")
            else:
                print("Producto no encontrado.")

        # ======================================================
        # 3. ACTUALIZAR PRODUCTO
        # ======================================================
        elif opcion == "3":
            sku = input("SKU del producto a actualizar: ").strip()

            print("Deje vacío el campo que no desea modificar.")

            stock = input("Nuevo stock: ").strip()
            precio_compra = input("Nuevo precio compra: ").strip()
            precio_venta = input("Nuevo precio venta: ").strip()

            try:
                actualizado = inventario.actualizar_producto(
                    sku=sku,
                    stock=int(stock) if stock else None,
                    precio_compra=float(precio_compra) if precio_compra else None,
                    precio_venta=float(precio_venta) if precio_venta else None
                )

                if actualizado:
                    print("Producto actualizado correctamente.")
                else:
                    print("Producto no encontrado.")

            except ValueError:
                print("Error: Datos numéricos inválidos.")

        # ======================================================
        # 4. BUSCAR PRODUCTO
        # ======================================================
        elif opcion == "4":
            texto = input("Ingrese nombre a buscar: ").strip()

            resultados = inventario.buscar_producto(texto)

            if not resultados:
                print("No se encontraron coincidencias.")
            else:
                print("\nResultados encontrados:\n")
                for p in resultados:
                    print(
                        f"SKU: {p.get_sku()} | "
                        f"Nombre: {p.get_nombre_producto()} | "
                        f"Stock: {p.get_stock_actual()} | "
                        f"Precio: {p.get_precio_venta()}"
                    )

        # ======================================================
        # 5. LISTAR TODOS LOS PRODUCTOS
        # ======================================================
        elif opcion == "5":
            productos = inventario.listar_todos()

            if not productos:
                print("El inventario está vacío.")
            else:
                print("\nListado completo del inventario:\n")
                for p in productos:
                    print(
                        f"SKU: {p.get_sku()} | "
                        f"Nombre: {p.get_nombre_producto()} | "
                        f"Stock: {p.get_stock_actual()} | "
                        f"Precio: {p.get_precio_venta()}"
                    )

        # ======================================================
        # 6. SALIR
        # ======================================================
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        # ======================================================
        # OPCIÓN INVÁLIDA
        # ======================================================
        else:
            print("Opción inválida. Intente nuevamente.")