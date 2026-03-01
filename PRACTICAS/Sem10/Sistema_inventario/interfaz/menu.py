from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    """
    Muestra las opciones disponibles del sistema.
    Esta función solo imprime el menú en pantalla.
    """
    print("""
    ===== SISTEMA DE GESTIÓN DE INVENTARIOS =====
    1. Registrar producto
    2. Dar de baja producto
    3. Actualizar stock / precios
    4. Buscar producto por SKU o nombre
    5. Listar todos los productos activos
    6. Listar todos los productos desactivados
    7. Salir
    """)


def ejecutar_menu():
    """
    Función principal del sistema en consola.

    - Crea una instancia del Inventario.
    - Controla el flujo del menú mediante un ciclo infinito.
    - Maneja validaciones y errores de entrada.
    """

    # Se crea el inventario.
    # En este momento ya se cargan automáticamente los datos del archivo.
    inventario = Inventario()

    # Ciclo principal del sistema
    while True:

        # Se muestra el menú en cada iteración
        mostrar_menu()

        # Se solicita la opción al usuario
        opcion = input("Seleccione una opción: ").strip()

        # ======================================================
        # 1. REGISTRAR PRODUCTO
        # ======================================================
        if opcion == "1":
            try:
                # Se solicitan los datos al usuario
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
                agregado = inventario.agregar_producto(producto)

                # Ahora el mensaje es más exacto
                if agregado:
                    print("✅ Producto registrado y guardado correctamente en archivo.")
                else:
                    print("   No se pudo registrar el producto.")
                    print("   Posibles causas:")
                    print("   - El SKU ya existe.")
                    print("   - Error al escribir en el archivo.")

            except ValueError as e:
                # Captura errores de conversión numérica o validaciones del Producto
                print(f"❌ Error en los datos ingresados: {e}")

        # ======================================================
        # 2. DAR DE BAJA PRODUCTO
        # ======================================================
        elif opcion == "2":

            sku = input("SKU del producto a desactivar: ").strip()

            resultado = inventario.desactivar_producto(sku)

            if resultado:
                print("✅ Producto desactivado y cambios guardados correctamente.")
            else:
                print("   No se pudo desactivar el producto.")
                print("   Posibles causas:")
                print("   - El SKU no existe.")
                print("   - El producto ya estaba inactivo.")
                print("   - Error al guardar en archivo.")

        # ======================================================
        # 3. ACTUALIZAR STOCK / PRECIOS
        # ======================================================
        elif opcion == "3":

            sku = input("SKU del producto: ").strip()

            print("Deja vacío lo que no deseas modificar.")

            stock = input("Nuevo stock: ").strip()
            precio_compra = input("Nuevo precio compra: ").strip()
            precio_venta = input("Nuevo precio venta: ").strip()

            try:
                # Solo se convierte a número si el usuario escribió algo
                actualizado = inventario.actualizar_producto(
                    sku=sku,
                    stock=int(stock) if stock else None,
                    precio_compra=float(precio_compra) if precio_compra else None,
                    precio_venta=float(precio_venta) if precio_venta else None
                )

                if actualizado:
                    print("✅ Producto actualizado y cambios guardados correctamente.")
                else:
                    print("   No se pudo actualizar el producto.")
                    print("   Posibles causas:")
                    print("   - El producto no existe.")
                    print("   - El producto está inactivo.")
                    print("   - Error al escribir en archivo.")

            except ValueError:
                # Error si el usuario ingresa texto en campos numéricos
                print("Error: Debes ingresar valores numéricos válidos.")

        # ======================================================
        # 4. BUSCAR PRODUCTO
        # ======================================================
        elif opcion == "4":

            texto = input("Buscar por SKU o nombre: ").strip()

            productos = inventario.buscar_producto(texto)

            if not productos:
                print("⚠ No se encontraron productos activos con ese criterio.")
            else:
                print("\nResultados encontrados:")
                for p in productos:
                    print(
                        f"{p.get_sku()} | {p.get_nombre_producto()} | "
                        f"Stock: {p.get_stock_actual()} | "
                        f"Precio venta: ${p.get_precio_venta()}"
                    )

        # ======================================================
        # 5. LISTAR PRODUCTOS ACTIVOS
        # ======================================================
        elif opcion == "5":

            productos = inventario.listar_activos()

            if not productos:
                print("⚠ No hay productos activos en el sistema.")
            else:
                print("\nListado de productos activos:")
                for p in productos:
                    print(
                        f"{p.get_sku()} | {p.get_nombre_producto()} | "
                        f"Stock: {p.get_stock_actual()} | "
                        f"Stock mínimo: {p.get_stock_minimo()} | ACTIVO"
                    )

        # ======================================================
        # 6. LISTAR PRODUCTOS INACTIVOS
        # ======================================================
        elif opcion == "6":

            productos = inventario.listar_inactivos()

            if not productos:
                print("No hay productos inactivos en el sistema.")
            else:
                print("\nListado de productos inactivos:")
                for p in productos:
                    print(
                        f"{p.get_sku()} | {p.get_nombre_producto()} | "
                        f"Stock: {p.get_stock_actual()} | "
                        f"Stock mínimo: {p.get_stock_minimo()} | INACTIVO"
                    )

        # ======================================================
        # 7. SALIR DEL SISTEMA
        # ======================================================
        elif opcion == "7":

            print("Saliendo del sistema...")
            break  # Termina el ciclo while

        # ======================================================
        # OPCIÓN INVÁLIDA
        # ======================================================
        else:
            print("Opción inválida. Intente nuevamente.")
