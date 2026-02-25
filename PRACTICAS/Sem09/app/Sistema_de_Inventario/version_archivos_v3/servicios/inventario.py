from modelos.producto import Producto


class Inventario:
    """
    Versión con persistencia en archivo de texto.
    Maneja lectura, escritura y excepciones.
    """

    def __init__(self):
        self.__archivo = "inventario.txt"
        self.__productos = {}  # clave = sku, valor = Producto
        self.cargar_desde_archivo()


    # ======================================================
    # CARGAR DESDE ARCHIVO
    # ======================================================
    def cargar_desde_archivo(self):
        self.__productos.clear()  # Limpia antes de volver a cargar datos
        try:
            with open(self.__archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split("|")

                    if len(datos) == 9:
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

        except FileNotFoundError:
            # Si no existe el archivo, lo crea vacío
            open(self.__archivo, "w").close()

        except PermissionError:
            print("❌ Error: No se tienen permisos para leer el archivo.")

        except Exception as e:
            print("❌ Error inesperado al cargar archivo:", e)

    # ======================================================
    # GUARDAR EN ARCHIVO
    # ======================================================
    def guardar_en_archivo(self):
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

        except PermissionError:
            print("❌ Error: No se tienen permisos para escribir en el archivo.")

        except Exception as e:
            print("❌ Error inesperado al guardar archivo:", e)

    # ======================================================
    # AGREGAR PRODUCTO
    # ======================================================
    def agregar_producto(self, producto: Producto):
        if producto.get_sku() in self.__productos:
            return False

        self.__productos[producto.get_sku()] = producto
        self.guardar_en_archivo()
        return True

    # ======================================================
    # DESACTIVAR PRODUCTO
    # ======================================================
    def desactivar_producto(self, sku):
        if sku in self.__productos:
            producto = self.__productos[sku]
            if producto.esta_activo():
                producto.desactivar()
                self.guardar_en_archivo()
                return True
        return False

    # ======================================================
    # ACTUALIZAR PRODUCTO
    # ======================================================
    def actualizar_producto(self, sku, stock=None, precio_compra=None, precio_venta=None):
        if sku in self.__productos:
            p = self.__productos[sku]

            if not p.esta_activo():
                return False

            if stock is not None:
                p.set_stock_actual(stock)

            if precio_compra is not None:
                p.set_precio_compra(precio_compra)

            if precio_venta is not None:
                p.set_precio_venta(precio_venta)

            self.guardar_en_archivo()
            return True

        return False

    # ======================================================
    # LISTAR PRODUCTOS ACTIVOS
    # ======================================================
    def listar_activos(self):
        return [
            p for p in self.__productos.values()
            if p.esta_activo()
        ]

    # ======================================================
    # LISTAR PRODUCTOS INACTIVOS
    # ======================================================
    def listar_inactivos(self):
        return [
            p for p in self.__productos.values()
            if not p.esta_activo()
        ]

    # ======================================================
    # BUSCAR PRODUCTO
    # ======================================================
    def buscar_producto(self, texto):
        texto = texto.lower()

        return [
            p for p in self.__productos.values()
            if p.esta_activo() and (
                    texto in p.get_sku().lower()
                    or texto in p.get_nombre_producto().lower()
            )
        ]
