from database.conexion import conectar

class Inventario:
    """
    Clase encargada de la lógica de negocio del inventario.

    Su responsabilidad es:
    - Comunicarse con la base de datos
    - Ejecutar operaciones CRUD (Create, Read, Update, Delete)
    - Separar la lógica de datos de la interfaz o del modelo Producto
    """

    def agregar_producto(self, producto):
        # Se abre una conexión a la base de datos
        conn = conectar()
        cursor = conn.cursor()

        try:
            # Se inserta un nuevo producto usando parámetros (?, ?, ?, ?)
            # Esto evita inyecciones SQL y errores de formato
            cursor.execute(
                "INSERT INTO productos (sku, nombre, cantidad, precio) VALUES (?, ?, ?, ?)",
                (
                    producto.get_sku(),
                    producto.get_nombre(),
                    producto.get_cantidad(),
                    producto.get_precio()
                )
            )

            # Se confirman los cambios
            conn.commit()
            print("Producto agregado correctamente")

        except:
            # Captura errores, principalmente cuando el SKU ya existe (UNIQUE)
            print("Error: SKU duplicado")

        finally:
            # Se cierra la conexión siempre, ocurra o no un error
            conn.close()

    def eliminar_producto(self, sku):
        # Conexión a la base de datos
        conn = conectar()
        cursor = conn.cursor()

        # Se elimina el producto según su SKU
        cursor.execute("DELETE FROM productos WHERE sku = ?", (sku,))
        conn.commit()

        # rowcount indica cuántas filas fueron afectadas
        if cursor.rowcount == 0:
            print("Producto no encontrado")
        else:
            print("Producto eliminado")

        conn.close()

    def actualizar_producto(self, sku, cantidad=None, precio=None):
        """
        Permite actualizar solo los campos necesarios.
        Si no se envía cantidad o precio, no se modifica ese campo.
        """

        conn = conectar()
        cursor = conn.cursor()

        # Actualiza cantidad solo si fue enviada
        if cantidad is not None:
            cursor.execute(
                "UPDATE productos SET cantidad = ? WHERE sku = ?",
                (cantidad, sku)
            )

        # Actualiza precio solo si fue enviado
        if precio is not None:
            cursor.execute(
                "UPDATE productos SET precio = ? WHERE sku = ?",
                (precio, sku)
            )

        conn.commit()

        # Verifica si se modificó algún registro
        if cursor.rowcount == 0:
            print("Producto no encontrado")
        else:
            print("Producto actualizado")

        conn.close()

    def buscar_producto(self, texto):
        """
        Busca productos por coincidencia parcial en:
        - nombre
        - SKU
        """

        conn = conectar()
        cursor = conn.cursor()

        # Se usa LIKE con comodines % para búsquedas flexibles
        cursor.execute("""
            SELECT id, sku, nombre, cantidad, precio
            FROM productos
            WHERE nombre LIKE ? OR sku LIKE ?
        """, (f"%{texto}%", f"%{texto}%"))

        resultados = cursor.fetchall()
        conn.close()

        # Se muestran los resultados encontrados
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos")

    def listar_productos(self):
        """
        Lista todos los productos del inventario
        """

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
