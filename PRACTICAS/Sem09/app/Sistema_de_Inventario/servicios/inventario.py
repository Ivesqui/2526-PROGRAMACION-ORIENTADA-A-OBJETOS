from database.conexion import conectar
from modelos.producto import Producto
from datetime import datetime

class Inventario:
    """
    Lógica de negocio del inventario.
    Todas las modificaciones de stock generan movimientos.
    """

    # ---------------------------------
    # REGISTRO DE MOVIMIENTOS
    # ---------------------------------
    def _registrar_movimiento(self, sku, tipo, cantidad, motivo):
        """
        Registra cualquier cambio de stock.

        Esto permite:
        - Auditoría
        - Trazabilidad
        - Confianza en el sistema
        """
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

    # ---------------------------------
    # AGREGAR PRODUCTO
    # ---------------------------------
    def agregar_producto(self, producto):
        conn = conectar()
        cursor = conn.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            cursor.execute("""
                INSERT INTO productos
                (sku, nombre, cantidad, precio, stock_minimo, fecha_creacion, fecha_actualizacion)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                producto.get_sku(),
                producto.get_nombre(),
                producto.get_cantidad(),
                producto.get_precio(),
                producto.get_stock_minimo(),
                fecha,
                fecha
            ))

            conn.commit()

            # Movimiento inicial
            self._registrar_movimiento(
                producto.get_sku(),
                "ENTRADA",
                producto.get_cantidad(),
                "Alta inicial de producto"
            )

            return True

        except Exception:
            return False

        finally:
            conn.close()

    # ---------------------------------
    # ACTUALIZAR STOCK
    # ---------------------------------
    def actualizar_stock(self, sku, nueva_cantidad, motivo="Ajuste manual"):
        """
        Actualiza el stock de un producto y registra el movimiento.
        """

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT cantidad FROM productos WHERE sku = ?", (sku,))
        fila = cursor.fetchone()

        if not fila:
            conn.close()
            return False

        cantidad_actual = fila[0]
        diferencia = nueva_cantidad - cantidad_actual

        tipo = "ENTRADA" if diferencia > 0 else "SALIDA"

        cursor.execute("""
            UPDATE productos
            SET cantidad = ?, fecha_actualizacion = ?
            WHERE sku = ?
        """, (
            nueva_cantidad,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sku
        ))

        conn.commit()
        conn.close()

        self._registrar_movimiento(
            sku,
            tipo,
            abs(diferencia),
            motivo
        )

        return True

    # ---------------------------------
    # CONSULTA DE MOVIMIENTOS
    # ---------------------------------
    def listar_movimientos(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT sku, tipo, cantidad, motivo, fecha
            FROM movimientos
            ORDER BY fecha DESC
        """)

        movimientos = cursor.fetchall()
        conn.close()
        return movimientos

