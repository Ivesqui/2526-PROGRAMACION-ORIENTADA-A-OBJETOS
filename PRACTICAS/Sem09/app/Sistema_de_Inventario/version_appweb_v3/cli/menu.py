# ======================================================
# CLI - MENÚ DE CONSOLA
# ======================================================
# Esta capa es SOLO presentación.
# No contiene lógica de negocio.
# Solo interactúa con el usuario y llama al Service.
# ======================================================

from core.entities.producto import Producto
from services.inventario_service import InventarioService
from infrastructure.repositories.sqlite_producto_repository import (
    SqliteProductoRepository
)
from infrastructure.database.conexion import crear_tablas


def mostrar_menu():
    """
    Muestra las opciones disponibles en consola.
    """
    print("""
    ===== SISTEMA DE GESTIÓN DE INVENTARIOS =====
    1. Registrar producto
    2. Dar de baja producto
    3. Actualizar stock / precios
    4. Buscar producto
    5. Listar inventario
    6. Registrar movimiento
    7. Ver movimientos (Kardex)
    8. Ver resumen dashboard
    9. Salir
    """)


def ejecutar_menu():
    """
    Punto de entrada del CLI.
    Se arma la inyección de dependencias aquí.
    """

    # Asegurar que existan las tablas
    crear_tablas()

    # Inyección de dependencias
    repo = SqliteProductoRepository()
    inventario = InventarioService(repo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        # ======================================================
        # 1. REGISTRAR PRODUCTO
        # ======================================================
        if opcion == "1":
            try:
                sku = input("SKU: ").strip()
                codigo_barras = input("Código de barras (opcional): ").strip() or None
                nombre = input("Nombre del producto: ").strip()
                categoria = input("Categoría: ").strip()
                unidad = input("Unidad (pieza, caja, kg, etc): ").strip()
                precio_compra = float(input("Precio de compra: "))
                precio_venta = float(input("Precio de venta: "))
                stock = int(input("Stock inicial: "))
                stock_minimo = int(input("Stock mínimo: "))

                producto = Producto(
                    sku=sku,
                    codigo_barras=codigo_barras,
                    nombre_producto=nombre,
                    categoria=categoria,
                    unidad=unidad,
                    precio_compra=precio_compra,
                    precio_venta=precio_venta,
                    stock_actual=stock,
                    stock_minimo=stock_minimo,
                    activo=True
                )

                creado = inventario.agregar_producto(producto)

                print("✅ Producto registrado correctamente"
                      if creado else
                      "❌ Error: SKU o código ya existe")

            except ValueError as e:
                print(f"❌ Error de datos: {e}")

        # ======================================================
        # 2. DAR DE BAJA PRODUCTO
        # ======================================================
        elif opcion == "2":
            sku = input("SKU del producto a desactivar: ").strip()

            eliminado = inventario.desactivar_producto(sku)

            print("✅ Producto dado de baja"
                  if eliminado else
                  "❌ Producto no encontrado")

        # ======================================================
        # 3. ACTUALIZAR PRODUCTO
        # ======================================================
        elif opcion == "3":
            sku = input("SKU del producto: ").strip()

            print("Deja vacío lo que no deseas modificar")

            stock = input("Nuevo stock: ")
            precio_compra = input("Nuevo precio compra: ")
            precio_venta = input("Nuevo precio venta: ")

            datos = {}

            if stock:
                datos["stock_actual"] = int(stock)
            if precio_compra:
                datos["precio_compra"] = float(precio_compra)
            if precio_venta:
                datos["precio_venta"] = float(precio_venta)

            actualizado = inventario.actualizar_parcial(sku, datos)

            print("✅ Producto actualizado"
                  if actualizado else
                  "❌ Producto no encontrado")

        # ======================================================
        # 4. BUSCAR PRODUCTO
        # ======================================================
        elif opcion == "4":
            texto = input("Buscar por SKU o nombre: ").strip()

            # Primero intentar por SKU
            producto = inventario.buscar_producto_por_sku(texto)

            if producto:
                print(producto)
            else:
                productos = inventario.buscar_por_nombre(texto)

                if not productos:
                    print("Sin resultados")
                else:
                    for p in productos:
                        print(p)

        # ======================================================
        # 5. LISTAR INVENTARIO
        # ======================================================
        elif opcion == "5":
            productos = inventario.listar_productos()

            if not productos:
                print("Inventario vacío")
            else:
                for p in productos:
                    print(p)

        # ======================================================
        # 6. REGISTRAR MOVIMIENTO
        # ======================================================
        elif opcion == "6":
            try:
                sku = input("SKU: ").strip()
                tipo = input("Tipo (ENTRADA/SALIDA/AJUSTE): ").strip().upper()
                cantidad = int(input("Cantidad: "))
                motivo = input("Motivo: ").strip()

                inventario.registrar_movimiento(
                    sku=sku,
                    tipo=tipo,
                    cantidad=cantidad,
                    motivo=motivo
                )

                print("✅ Movimiento registrado")

            except ValueError as e:
                print(f"❌ Error: {e}")

        # ======================================================
        # 7. VER MOVIMIENTOS
        # ======================================================
        elif opcion == "7":
            sku = input("SKU del producto: ").strip()

            movimientos = inventario.obtener_movimientos_por_sku(sku)

            if not movimientos:
                print("Sin movimientos")
            else:
                for m in movimientos:
                    print(m)

        # ======================================================
        # 8. DASHBOARD
        # ======================================================
        elif opcion == "8":
            resumen = inventario.obtener_resumen_dashboard()

            print("===== RESUMEN =====")
            print(f"Total productos: {resumen['total_productos']}")
            print(f"Productos críticos: {resumen['productos_criticos']}")
            print(f"Valor total inventario: ${resumen['valor_total_inventario']}")

        # ======================================================
        # 9. SALIR
        # ======================================================
        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida")