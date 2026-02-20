from modelos.producto import Producto
from servicios.inventario import Inventario
from reportes.reporte_excel import generar_excel_inventario


def mostrar_menu():
    print("""
    ===== SISTEMA DE GESTIÓN DE INVENTARIOS =====
    1. Registrar producto
    2. Dar de baja producto
    3. Actualizar stock / precios
    4. Buscar producto
    5. Listar inventario
    6. Exportar inventario a Excel
    7. Salir
    """)


def ejecutar_menu():
    inventario = Inventario()

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

                if inventario.agregar_producto(producto):
                    print("✅ Producto registrado correctamente")
                else:
                    print("❌ Error: SKU ya existe")

            except ValueError as e:
                print(f"❌ Error de datos: {e}")

        # ======================================================
        # 2. DAR DE BAJA PRODUCTO
        # ======================================================
        elif opcion == "2":
            sku = input("SKU del producto a desactivar: ").strip()

            if inventario.desactivar_producto(sku):
                print("✅ Producto dado de baja")
            else:
                print("❌ Producto no encontrado")

        # ======================================================
        # 3. ACTUALIZAR STOCK / PRECIOS
        # ======================================================
        elif opcion == "3":
            sku = input("SKU del producto: ").strip()

            print("Deja vacío lo que no deseas modificar")
            stock = input("Nuevo stock: ")
            precio_compra = input("Nuevo precio compra: ")
            precio_venta = input("Nuevo precio venta: ")

            actualizado = inventario.actualizar_producto(
                sku=sku,
                stock=int(stock) if stock else None,
                precio_compra=float(precio_compra) if precio_compra else None,
                precio_venta=float(precio_venta) if precio_venta else None
            )

            print("✅ Producto actualizado" if actualizado else "❌ Producto no encontrado")

        # ======================================================
        # 4. BUSCAR PRODUCTO
        # ======================================================
        elif opcion == "4":
            texto = input("Buscar por SKU o nombre: ").strip()
            productos = inventario.buscar_producto(texto)

            if not productos:
                print("Sin resultados")
            else:
                for p in productos:
                    print(
                        f"{p.get_sku()} | {p.get_nombre_producto()} | "
                        f"Stock: {p.get_stock_actual()} | "
                        f"Venta: ${p.get_precio_venta()}"
                    )

        # ======================================================
        # 5. LISTAR INVENTARIO
        # ======================================================
        elif opcion == "5":
            productos = inventario.listar_productos()

            if not productos:
                print("Inventario vacío")
            else:
                for p in productos:
                    estado = "ACTIVO" if p.esta_activo() else "INACTIVO"
                    print(
                        f"{p.get_sku()} | {p.get_nombre_producto()} | "
                        f"Stock: {p.get_stock_actual()} | "
                        f"Mín: {p.get_stock_minimo()} | "
                        f"{estado}"
                    )

        # ======================================================
        # 6. EXPORTAR EXCEL
        # ======================================================
        elif opcion == "6":
            generar_excel_inventario()
            print("📊 Excel generado correctamente")

        # ======================================================
        # 7. SALIR
        # ======================================================
        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida")
