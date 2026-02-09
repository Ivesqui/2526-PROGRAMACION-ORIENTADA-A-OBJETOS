from database.conexion import conectar

class Inventario:

    def agregar_producto(self, producto):
        conn = conectar()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO productos VALUES (?, ?, ?, ?)",
                (producto.get_id(), producto.get_nombre(),
                 producto.get_cantidad(), producto.get_precio())
            )
            conn.commit()
            print("✅ Producto agregado correctamente")
        except:
            print("❌ Error: ID duplicado")
        finally:
            conn.close()

    def eliminar_producto(self, id_producto):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()

        if cursor.rowcount == 0:
            print("Producto no encontrado")
        else:
            print("Producto eliminado")

        conn.close()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        conn = conectar()
        cursor = conn.cursor()

        if cantidad is not None:
            cursor.execute(
                "UPDATE productos SET cantidad = ? WHERE id = ?",
                (cantidad, id_producto)
            )

        if precio is not None:
            cursor.execute(
                "UPDATE productos SET precio = ? WHERE id = ?",
                (precio, id_producto)
            )

        conn.commit()

        if cursor.rowcount == 0:
            print("Producto no encontrado")
        else:
            print("Producto actualizado")

        conn.close()

    def buscar_producto(self, nombre):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM productos WHERE nombre LIKE ?",
            (f"%{nombre}%",)
        )

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
