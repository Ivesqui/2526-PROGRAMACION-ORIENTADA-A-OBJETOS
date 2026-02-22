import sqlite3
from typing import List, Optional
from core.entities.producto import Producto
from core.interfaces.producto_repository import ProductoRepository


class SqliteProductoRepository(ProductoRepository):

    def __init__(self, db_path="inventario.db"):
        self.db_path = db_path

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def guardar(self, producto: Producto):
        conn = self._conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO productos (
                sku, codigo_barras, nombre_producto, categoria,
                descripcion, unidad, precio_compra, precio_venta,
                stock_actual, stock_minimo, activo,
                fecha_creacion, fecha_actualizacion
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            producto.sku,
            producto.codigo_barras,
            producto.nombre_producto,
            producto.categoria,
            producto.descripcion,
            producto.unidad,
            producto.precio_compra,
            producto.precio_venta,
            producto.stock_actual,
            producto.stock_minimo,
            int(producto.activo),
            producto.fecha_creacion,
            producto.fecha_actualizacion
        ))

        conn.commit()
        conn.close()

    def obtener_todos(self) -> List[Producto]:
        conn = self._conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM productos WHERE activo = 1
        """)

        filas = cursor.fetchall()
        conn.close()

        productos = []
        for fila in filas:
            productos.append(Producto(
                sku=fila[1],
                codigo_barras=fila[2],
                nombre_producto=fila[3],
                categoria=fila[4],
                descripcion=fila[5],
                unidad=fila[6],
                precio_compra=fila[7],
                precio_venta=fila[8],
                stock_actual=fila[9],
                stock_minimo=fila[10],
                activo=bool(fila[11]),
                fecha_creacion=fila[12]
            ))

        return productos

    def obtener_por_sku(self, sku: str) -> Optional[Producto]:
        conn = self._conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM productos WHERE sku = ? AND activo = 1
        """, (sku,))

        fila = cursor.fetchone()
        conn.close()

        if not fila:
            return None

        return Producto(
            sku=fila[1],
            codigo_barras=fila[2],
            nombre_producto=fila[3],
            categoria=fila[4],
            descripcion=fila[5],
            unidad=fila[6],
            precio_compra=fila[7],
            precio_venta=fila[8],
            stock_actual=fila[9],
            stock_minimo=fila[10],
            activo=bool(fila[11]),
            fecha_creacion=fila[12]
        )

    def actualizar(self, producto: Producto):
        conn = self._conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE productos
            SET codigo_barras = ?,
                nombre_producto = ?,
                categoria = ?,
                descripcion = ?,
                unidad = ?,
                precio_compra = ?,
                precio_venta = ?,
                stock_actual = ?,
                stock_minimo = ?,
                fecha_actualizacion = ?
            WHERE sku = ?
        """, (
            producto.codigo_barras,
            producto.nombre_producto,
            producto.categoria,
            producto.descripcion,
            producto.unidad,
            producto.precio_compra,
            producto.precio_venta,
            producto.stock_actual,
            producto.stock_minimo,
            producto.fecha_actualizacion,
            producto.sku
        ))

        conn.commit()
        conn.close()

    def eliminar_logico(self, sku: str):
        conn = self._conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE productos
            SET activo = 0
            WHERE sku = ?
        """, (sku,))

        conn.commit()
        conn.close()