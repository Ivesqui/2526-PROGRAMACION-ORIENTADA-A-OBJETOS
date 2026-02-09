from database.conexion import conectar
from modelos.producto import Producto

class Inventario:
    """
    Clase que gestiona la lógica de acceso a datos del inventario.
    NO imprime mensajes, solo devuelve resultados.
    """

    def agregar_producto(self, producto):
        """
        Inserta un producto en la base de datos.

        Retorna:
        - True si se insertó correctamente
        - False si ocurrió un error (ej. SKU duplicado)
        """
        conn = conectar()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO productos (sku, nombre, cantidad, precio) VALUES (?, ?, ?, ?)",
                (
                    producto.get_sku(),
                    producto.get_nombre(),
                    producto.get_cantidad(),
                    producto.get_precio()
                )
            )
            conn.commit()
            return True

        except Exception:
            # Error típico: violación de restricción UNIQUE (SKU duplicado)
            return False

        finally:
            conn.close()

    def eliminar_producto(self, sku):
        """
        Elimina un producto usando el SKU.

        Retorna:
        - True si se eliminó
        - False si no se encontró el producto
        """
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE sku = ?", (sku,))
        conn.commit()

        eliminado = cursor.rowcount > 0
        conn.close()

        return eliminado

    def actualizar_producto(self, sku, cantidad=None, precio=None):
        """
        Actualiza cantidad y/o precio de un producto identificado por SKU.

        Parámetros opcionales permiten actualizar solo lo necesario.

        Retorna:
        - True si se actualizó
        - False si no se encontró el producto
        """
        conn = conectar()
        cursor = conn.cursor()

        if cantidad is not None:
            cursor.execute(
                "UPDATE productos SET cantidad = ? WHERE sku = ?",
                (cantidad, sku)
            )

        if precio is not None:
            cursor.execute(
                "UPDATE productos SET precio = ? WHERE sku = ?",
                (precio, sku)
            )

        conn.commit()
        actualizado = cursor.rowcount > 0
        conn.close()

        return actualizado

    def buscar_producto(self, texto):
        """
        Busca productos por nombre o SKU.

        Retorna:
        - Lista de objetos Producto
        """
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT sku, nombre, cantidad, precio
            FROM productos
            WHERE nombre LIKE ? OR sku LIKE ?
        """, (f"%{texto}%", f"%{texto}%"))

        filas = cursor.fetchall()
        conn.close()

        # Convertimos cada fila en un objeto Producto
        productos = [
            Producto(f[0], f[1], f[2], f[3])
            for f in filas
        ]

        return productos

    def listar_productos(self):
        """
        Retorna todo el inventario como una lista de objetos Producto.
        """
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT sku, nombre, cantidad, precio FROM productos")
        filas = cursor.fetchall()
        conn.close()

        return [
            Producto(f[0], f[1], f[2], f[3])
            for f in filas
        ]

