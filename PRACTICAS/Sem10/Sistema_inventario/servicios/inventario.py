from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar los productos del sistema.

    Responsabilidades:
    - Mantener productos en memoria.
    - Persistirlos en archivo de texto.
    - Manejar errores de lectura y escritura.
    - Retornar estados reales de éxito o fallo.
    """

    def __init__(self):
        self.__archivo = "inventario.txt"
        self.__productos = {}

        # Cargar productos al iniciar
        self.cargar_desde_archivo()

    # ======================================================
    # CARGAR DESDE ARCHIVO
    # ======================================================
    def cargar_desde_archivo(self):
        """
        Carga productos desde archivo.
        No devuelve estado porque el sistema puede seguir funcionando
        incluso si el archivo no existe.
        """

        self.__productos.clear()

        try:
            with open(self.__archivo, "r", encoding="utf-8") as archivo:

                for numero_linea, linea in enumerate(archivo, start=1):

                    try:
                        datos = linea.strip().split("|")

                        if len(datos) != 9:
                            raise ValueError("Formato incorrecto")

                        producto = Producto(
                            sku=datos[0],
                            nombre_producto=datos[1],
                            categoria=datos[2],
                            unidad=datos[3],
                            precio_compra=float(datos[4]),
                            precio_venta=float(datos[5]),
                            stock_actual=int(datos[6]),
                            stock_minimo=int(datos[7]),
                            activo=datos[8] == "True"
                        )

                        self.__productos[producto.get_sku()] = producto

                    except Exception as e:
                        print(f"Línea {numero_linea} ignorada (archivo corrupto): {e}")

        except FileNotFoundError:
            # Si no existe el archivo lo crea vacío
            print("Archivo no encontrado. Se creará uno nuevo.")
            try:
                open(self.__archivo, "w").close()
            except Exception as e:
                print("No se pudo crear el archivo:", e)

        except PermissionError:
            print("No hay permisos para leer el archivo.")

        except Exception as e:
            print("Error inesperado al cargar archivo:", e)

    # ======================================================
    # GUARDAR EN ARCHIVO
    # ======================================================
    def guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo.

        Retorna:
            True  -> si se guardó correctamente
            False -> si ocurrió un error
        """

        try:
            with open(self.__archivo, "w", encoding="utf-8") as archivo:

                for p in self.__productos.values():

                    linea = "|".join([
                        p.get_sku(),
                        p.get_nombre_producto(),
                        p.get_categoria(),
                        p.get_unidad(),
                        str(p.get_precio_compra()),
                        str(p.get_precio_venta()),
                        str(p.get_stock_actual()),
                        str(p.get_stock_minimo()),
                        str(p.esta_activo())
                    ])

                    archivo.write(linea + "\n")

            # Si todo salió bien
            return True

        except PermissionError:
            print("No se tienen permisos para escribir en el archivo.")
            return False

        except Exception as e:
            print("Error inesperado al guardar archivo:", e)
            return False

    # ======================================================
    # MÉTODOS DE GESTIÓN
    # ======================================================

    def agregar_producto(self, producto: Producto):
        """
        Agrega un producto al inventario.

        Retorna:
            True  -> agregado y guardado correctamente
            False -> SKU duplicado o error de escritura
        """

        if producto.get_sku() in self.__productos:
            return False

        self.__productos[producto.get_sku()] = producto

        # Solo retorna True si realmente se guardó
        if self.guardar_en_archivo():
            return True
        else:
            # Si falla la escritura, se revierte el cambio en memoria
            del self.__productos[producto.get_sku()]
            return False

    def desactivar_producto(self, sku):
        """
        Desactiva un producto.

        Retorna:
            True  -> desactivado y guardado correctamente
            False -> no existe, ya estaba inactivo o error de escritura
        """

        if sku not in self.__productos:
            return False

        producto = self.__productos[sku]

        if not producto.esta_activo():
            return False

        producto.desactivar()

        if self.guardar_en_archivo():
            return True
        else:
            # Si falla la escritura, se revierte el cambio
            producto._Producto__activo = True
            return False

    def eliminar_producto(self, sku):
        """
        Elimina completamente un producto del inventario
        (eliminación física, no lógica).

        Retorna:
            True  -> eliminado y guardado correctamente
            False -> no existe o error de escritura
        """

        # Verificamos si el producto existe
        if sku not in self.__productos:
            return False

        # Guardamos el producto por seguridad (por si hay que revertir)
        producto_eliminado = self.__productos[sku]

        # Eliminamos de memoria
        del self.__productos[sku]

        # Intentamos guardar cambios en archivo
        if self.guardar_en_archivo():
            return True
        else:
            # Si falla la escritura, revertimos el cambio
            self.__productos[sku] = producto_eliminado
            return False

    def actualizar_producto(self, sku, stock=None, precio_compra=None, precio_venta=None):
        """
        Actualiza datos de un producto activo.

        Retorna:
            True  -> actualizado y guardado correctamente
            False -> producto no encontrado, inactivo o error de escritura
        """

        if sku not in self.__productos:
            return False

        producto = self.__productos[sku]

        if not producto.esta_activo():
            return False

        # Guardamos valores anteriores por seguridad
        stock_anterior = producto.get_stock_actual()
        precio_compra_anterior = producto.get_precio_compra()
        precio_venta_anterior = producto.get_precio_venta()

        try:
            if stock is not None:
                producto.set_stock_actual(stock)

            if precio_compra is not None:
                producto.set_precio_compra(precio_compra)

            if precio_venta is not None:
                producto.set_precio_venta(precio_venta)

        except Exception:
            return False

        if self.guardar_en_archivo():
            return True
        else:
            # Si falla la escritura, revertimos cambios
            producto.set_stock_actual(stock_anterior)
            producto.set_precio_compra(precio_compra_anterior)
            producto.set_precio_venta(precio_venta_anterior)
            return False

    def listar_activos(self):
        return [p for p in self.__productos.values() if p.esta_activo()]

    def listar_inactivos(self):
        return [p for p in self.__productos.values() if not p.esta_activo()]

    def buscar_producto(self, texto):
        texto = texto.lower()

        return [
            p for p in self.__productos.values()
            if p.esta_activo() and (
                texto in p.get_sku().lower()
                or texto in p.get_nombre_producto().lower()
            )
        ]