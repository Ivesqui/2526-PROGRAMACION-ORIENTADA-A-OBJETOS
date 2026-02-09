from database.conexion import conectar

class Inventario:

    def agregar_producto(self, producto):
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
            print("Producto agregado correctamente")
        except:
            print("Error: SKU duplicado")
        finally:
            conn.close()

    def eliminar_producto(self, sku):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE sku = ?", (sku,))
        conn.commit()

        if cursor.rowcount == 0:
            print("Producto no encontrado")
        else:
            print("Producto eliminado")

        conn.close()

    def actualizar_producto(self, sku, cantidad=None, precio=None):
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

        if cursor.rowcount == 0:
            print("Producto no encontrado...")
        else:
            print("Producto actualizado...")

        conn.close()

        if cursor.rowcount == 0:
            print("Producto no encontrado")
        else:
            print("Producto actualizado")

        conn.close()

    def buscar_producto(self, texto):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, sku, nombre, cantidad, precio
            FROM productos
            WHERE nombre LIKE ? OR sku LIKE ?
        """, (f"%{texto}%", f"%{texto}%"))

        resultados = cursor.fetchall()
        conn.close()

        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos")

    def listar_productos(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()

        if productos:
            for p in productos:
                print(p)
        else:
            print("Inventario vacío")
