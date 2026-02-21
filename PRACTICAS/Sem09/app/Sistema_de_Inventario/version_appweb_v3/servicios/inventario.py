from datetime import datetime
from database.conexion import conectar
from modelos.producto import Producto


class Inventario:
    """
    Capa de lógica de negocio del inventario.
    Toda interacción con la BD pasa por aquí.
    """

    # ======================================================
    # REGISTRAR MOVIMIENTO (KARDEX)
    # ======================================================
    def _registrar_movimiento(self, sku, tipo, cantidad, motivo):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO movimientos (sku, tipo, cantidad, motivo, fecha)
            VALUES (?, ?, ?, ?, ?)
        """, (
            sku,
            tipo,
            cantidad,
            motivo,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

    # ======================================================
    # REGISTRAR PRODUCTO
    # ======================================================
    def agregar_producto(self, producto: Producto):
        conn = conectar()
        cursor = conn.cursor()
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            cursor.execute("""
                INSERT INTO productos (
                    sku,
                    codigo_barras,
                    nombre_producto,
                    categoria,
                    unidad,
                    precio_compra,
                    precio_venta,
                    stock_actual,
                    stock_minimo,
                    activo,
                    fecha_creacion,
                    fecha_actualizacion
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                producto.get_sku(),
                producto.get_codigo_barras(),
                producto.get_nombre_producto(),
                producto.get_categoria(),
                producto.get_unidad(),
                producto.get_precio_compra(),
                producto.get_precio_venta(),
                producto.get_stock_actual(),
                producto.get_stock_minimo(),
                1,
                ahora,
                ahora
            ))

            conn.commit()

            # Movimiento inicial
            self._registrar_movimiento(
                producto.get_sku(),
                "ENTRADA",
                producto.get_stock_actual(),
                "Registro inicial del producto"
            )

            return True

        except Exception as e:
            print("ERROR BD:", e)
            return False

        finally:
            conn.close()

    # ======================================================
    # DAR DE BAJA (NO BORRA)
    # ======================================================
    def desactivar_producto(self, sku):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE productos
            SET activo = 0, fecha_actualizacion = ?
            WHERE sku = ?
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sku
        ))

        conn.commit()
        filas = cursor.rowcount
        conn.close()

        return filas > 0

    # ======================================================
    # ACTUALIZAR STOCK / PRECIOS / CODIGO_BARRAS
    # ======================================================
    def actualizar_producto(
        self,
        sku,
        stock=None,
        precio_compra=None,
        precio_venta=None,
        codigo_barras=None
    ):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT stock_actual, precio_compra, precio_venta, codigo_barras
            FROM productos
            WHERE sku = ? AND activo = 1
        """, (sku,))

        fila = cursor.fetchone()
        if not fila:
            conn.close()
            return False

        stock_actual, pc_actual, pv_actual, cb_actual = fila

        stock_final = stock if stock is not None else stock_actual
        pc_final = precio_compra if precio_compra is not None else pc_actual
        pv_final = precio_venta if precio_venta is not None else pv_actual
        cb_final = codigo_barras if codigo_barras is not None else cb_actual

        try:
            cursor.execute("""
                UPDATE productos
                SET
                    stock_actual = ?,
                    precio_compra = ?,
                    precio_venta = ?,
                    codigo_barras = ?,
                    fecha_actualizacion = ?
                WHERE sku = ?
            """, (
                stock_final,
                pc_final,
                pv_final,
                cb_final,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                sku
            ))

            conn.commit()
            return True

        except Exception as e:
            print("ERROR al actualizar:", e)
            return False

        finally:
            conn.close()

    # ======================================================
    # LISTAR INVENTARIO
    # ======================================================
    def listar_productos(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                sku,
                codigo_barras,
                nombre_producto,
                categoria,
                unidad,
                precio_compra,
                precio_venta,
                stock_actual,
                stock_minimo,
                activo
            FROM productos
            ORDER BY nombre_producto
        """)

        filas = cursor.fetchall()
        conn.close()

        productos = []
        for f in filas:
            productos.append(
                Producto(
                    sku=f[0],
                    codigo_barras=f[1],
                    nombre_producto=f[2],
                    categoria=f[3],
                    unidad=f[4],
                    precio_compra=f[5],
                    precio_venta=f[6],
                    stock_actual=f[7],
                    stock_minimo=f[8],
                    activo=bool(f[9])
                )
            )

        return productos

    # ======================================================
    # BUSCAR PRODUCTO (SKU, NOMBRE o CODIGO_BARRAS)
    # ======================================================
    def buscar_producto(self, texto):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                sku,
                codigo_barras,
                nombre_producto,
                categoria,
                unidad,
                precio_compra,
                precio_venta,
                stock_actual,
                stock_minimo,
                activo
            FROM productos
            WHERE sku LIKE ?
               OR nombre_producto LIKE ?
               OR codigo_barras LIKE ?
        """, (f"%{texto}%", f"%{texto}%", f"%{texto}%"))

        filas = cursor.fetchall()
        conn.close()

        productos = []
        for f in filas:
            productos.append(
                Producto(
                    sku=f[0],
                    codigo_barras=f[1],
                    nombre_producto=f[2],
                    categoria=f[3],
                    unidad=f[4],
                    precio_compra=f[5],
                    precio_venta=f[6],
                    stock_actual=f[7],
                    stock_minimo=f[8],
                    activo=bool(f[9])
                )
            )

        return productos

    # ======================================================
    # BUSCAR POR CODIGO DE BARRAS EXACTO (IDEAL PARA ESCANER)
    # ======================================================
    def buscar_por_codigo_barras(self, codigo):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                sku,
                codigo_barras,
                nombre_producto,
                categoria,
                unidad,
                precio_compra,
                precio_venta,
                stock_actual,
                stock_minimo,
                activo
            FROM productos
            WHERE codigo_barras = ?
              AND activo = 1
        """, (codigo,))

        fila = cursor.fetchone()
        conn.close()

        if not fila:
            return None

        return Producto(
            sku=fila[0],
            codigo_barras=fila[1],
            nombre_producto=fila[2],
            categoria=fila[3],
            unidad=fila[4],
            precio_compra=fila[5],
            precio_venta=fila[6],
            stock_actual=fila[7],
            stock_minimo=fila[8],
            activo=bool(fila[9])
        )

    # ======================================================
    # BUSCAR POR NOMBRE DE PRODUCTO
    # ======================================================
    def buscar_por_nombre(self, nombre):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM productos
            WHERE nombre_producto LIKE ?
        """, (f"%{nombre}%",))

        filas = cursor.fetchall()
        conn.close()

        productos = []

        for fila in filas:
            producto = Producto(
            sku=fila[0],
            codigo_barras=fila[1],
            nombre_producto=fila[2],
            categoria=fila[3],
            unidad=fila[4],
            precio_compra=fila[5],
            precio_venta=fila[6],
            stock_actual=fila[7],
            stock_minimo=fila[8],
            activo=bool(fila[9])
        )
        productos.append(producto)

        return productos