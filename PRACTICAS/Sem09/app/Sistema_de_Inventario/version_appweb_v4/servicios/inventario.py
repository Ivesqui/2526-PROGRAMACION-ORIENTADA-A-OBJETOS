from datetime import datetime
from database.conexion import conectar
from modelos.producto import Producto


class Inventario:

    # ======================================================
    # REGISTRAR MOVIMIENTO PRIVADO
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
    # AGREGAR PRODUCTO
    # ======================================================
    def agregar_producto(self, producto: Producto):
        conn = conectar()
        cursor = conn.cursor()
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            cursor.execute("""
                INSERT INTO productos (
                    sku, codigo_barras, nombre_producto,
                    categoria, unidad,
                    precio_compra, precio_venta,
                    stock_actual, stock_minimo,
                    activo, fecha_creacion, fecha_actualizacion
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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

            self._registrar_movimiento(
                producto.get_sku(),
                "ENTRADA",
                producto.get_stock_actual(),
                "Registro inicial"
            )

            return True

        except Exception as e:
            print("ERROR BD:", e)
            return False

        finally:
            conn.close()


    # ======================================================
    # REGISTRAR MOVIMIENTO PUBLICO
    # ======================================================
    def registrar_movimiento(self, sku, tipo, cantidad, motivo=""):
        conn = conectar()
        cursor = conn.cursor()

        productos = self.buscar_producto(sku)

        if not productos:
            conn.close()
            return None

        producto = productos[0]
        stock_actual = producto.get_stock_actual()

        if tipo == "ENTRADA":
            nuevo_stock = stock_actual + cantidad
        elif tipo == "SALIDA":
            if cantidad > stock_actual:
                conn.close()
                raise ValueError("Stock insuficiente")
            nuevo_stock = stock_actual - cantidad
        else:
            conn.close()
            raise ValueError("Tipo inválido")

        cursor.execute("""
            UPDATE productos
            SET stock_actual = ?, fecha_actualizacion = ?
            WHERE sku = ?
        """, (
            nuevo_stock,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sku
        ))

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

        return True


    # ======================================================
    # ACTUALIZAR PARCIAL SEGURO
    # ======================================================
    def actualizar_parcial(self, sku, datos):
        conn = conectar()
        cursor = conn.cursor()

        campos_permitidos = {
            "precio_compra", "precio_venta", "stock_actual",
            "codigo_barras", "stock_minimo",
            "categoria", "unidad", "nombre_producto"
        }

        datos_filtrados = {
            k: v for k, v in datos.items()
            if k in campos_permitidos
        }

        if not datos_filtrados:
            conn.close()
            return None

        campos = []
        valores = []

        for campo, valor in datos_filtrados.items():
            campos.append(f"{campo} = ?")
            valores.append(valor)

        valores.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        valores.append(sku)

        cursor.execute(f"""
            UPDATE productos
            SET {", ".join(campos)}, fecha_actualizacion = ?
            WHERE sku = ?
        """, valores)

        conn.commit()
        conn.close()

        return True


    # ======================================================
    # DESACTIVAR
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
    # LISTAR
    # ======================================================
    def listar_productos(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT sku, codigo_barras, nombre_producto,
                   categoria, unidad,
                   precio_compra, precio_venta,
                   stock_actual, stock_minimo, activo
            FROM productos
            ORDER BY nombre_producto
        """)

        filas = cursor.fetchall()
        conn.close()

        productos = []

        for f in filas:
            productos.append(Producto(
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
            ))

        return productos


    # ======================================================
    # BUSCAR GENERICO
    # ======================================================
    def buscar_producto(self, texto):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT sku, codigo_barras, nombre_producto,
                   categoria, unidad,
                   precio_compra, precio_venta,
                   stock_actual, stock_minimo, activo
            FROM productos
            WHERE sku LIKE ?
               OR nombre_producto LIKE ?
               OR codigo_barras LIKE ?
        """, (f"%{texto}%", f"%{texto}%", f"%{texto}%"))

        filas = cursor.fetchall()
        conn.close()

        productos = []

        for f in filas:
            productos.append(Producto(
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
            ))

        return productos


    # ======================================================
    # KARDEX
    # ======================================================
    def obtener_movimientos_por_sku(self, sku):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, sku, tipo, cantidad, motivo, fecha
            FROM movimientos
            WHERE sku = ?
            ORDER BY fecha DESC
        """, (sku,))

        filas = cursor.fetchall()
        conn.close()

        return [
            {
                "id": f[0],
                "sku": f[1],
                "tipo": f[2],
                "cantidad": f[3],
                "motivo": f[4],
                "fecha": f[5]
            }
            for f in filas
        ]