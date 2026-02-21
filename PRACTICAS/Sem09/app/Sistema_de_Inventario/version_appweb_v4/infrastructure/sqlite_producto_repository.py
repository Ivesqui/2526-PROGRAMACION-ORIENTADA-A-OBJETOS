import sqlite3
from typing import List, Optional
from core.interfaces.i_producto_repository import IProductoRepository
from core.entities.producto import Producto
from database.conexion import conectar


class SQLiteProductoRepository(IProductoRepository):
    """
    Implementación específica para SQLite.
    Si mañana usas PostgreSQL, solo creas otra clase similar.
    """

    def guardar(self, p: Producto) -> bool:
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO productos (sku, nombre_producto, categoria, unidad, precio_compra, 
                                     precio_venta, stock_actual, stock_minimo, activo, codigo_barras)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (p.sku, p.nombre, p.categoria, p.unidad, p.precio_compra,
                  p.precio_venta, p.stock, p.stock_minimo, 1 if p.activo else 0, p.codigo_barras))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    def obtener_por_sku(self, sku: str) -> Optional[Producto]:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE sku = ?", (sku,))
        f = cursor.fetchone()
        conn.close()

        if f:
            # Mapeamos la fila de la DB a la Entidad del Core
            return Producto(
                sku=f[1], nombre_producto=f[3], categoria=f[4], unidad=f[6],
                precio_compra=f[7], precio_venta=f[8], stock_actual=f[9],
                stock_minimo=f[10], activo=bool(f[11]), codigo_barras=f[2]
            )
        return None

    def listar_todos(self) -> List[Producto]:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE activo = 1")
        filas = cursor.fetchall()
        conn.close()

        return [Producto(
            sku=f[1], nombre_producto=f[3], categoria=f[4], unidad=f[6],
            precio_compra=f[7], precio_venta=f[8], stock_actual=f[9],
            stock_minimo=f[10], activo=bool(f[11]), codigo_barras=f[2]
        ) for f in filas]

    def actualizar_stock(self, sku: str, nueva_cantidad: int) -> bool:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET stock_actual = ? WHERE sku = ?", (nueva_cantidad, sku))
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success