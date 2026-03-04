# ======================================================
# IMPORTACIONES
# ======================================================

from modelos.producto import Producto


# ======================================================
# CLASE INVENTARIO
# ======================================================
class Inventario:
    """
    Gestiona el inventario usando:
    - Diccionario (almacenamiento principal)
    - Set (control de SKUs únicos)
    - Listas (resultados)
    - Archivo TXT plano (sin formato JSON)
    """

    # ======================================================
    # CONSTRUCTOR
    # ======================================================
    def __init__(self):

        self.__archivo = "inventario.txt"

        self.__productos = {}
        self.__skus = set()

        self.cargar_desde_archivo()

    # ======================================================
    # GUARDAR EN ARCHIVO (FORMATO PLANO)
    # ======================================================
    def guardar_en_archivo(self):
        """
        Guarda cada producto en una línea
        separando atributos con |
        """

        try:
            with open(self.__archivo, "w", encoding="utf-8") as archivo:

                for p in self.__productos.values():
                    linea = (
                        f"{p.get_sku()}|"
                        f"{p.get_nombre_producto()}|"
                        f"{p.get_categoria()}|"
                        f"{p.get_unidad()}|"
                        f"{p.get_precio_compra()}|"
                        f"{p.get_precio_venta()}|"
                        f"{p.get_stock_actual()}|"
                        f"{p.get_stock_minimo()}|"
                        f"{p.esta_activo()}\n"
                    )

                    archivo.write(linea)

        except Exception as e:
            print("Error al guardar archivo:", e)

    # ======================================================
    # CARGAR DESDE ARCHIVO
    # ======================================================
    def cargar_desde_archivo(self):
        """
        Lee el archivo línea por línea
        y reconstruye los objetos Producto.
        """

        self.__productos.clear()
        self.__skus.clear()

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
                        self.__skus.add(producto.get_sku())

        except FileNotFoundError:
            # Si no existe, lo crea vacío
            with open(self.__archivo, "w", encoding="utf-8"):
                pass

        except Exception as e:
            print("Error al cargar archivo:", e)

    # ======================================================
    # AGREGAR PRODUCTO
    # ======================================================
    def agregar_producto(self, producto: Producto):

        if producto.get_sku() in self.__skus:
            return False

        self.__productos[producto.get_sku()] = producto
        self.__skus.add(producto.get_sku())

        self.guardar_en_archivo()
        return True

    # ======================================================
    # ELIMINACIÓN FÍSICA
    # ======================================================
    def eliminar_producto(self, sku):

        if sku in self.__productos:
            del self.__productos[sku]
            self.__skus.remove(sku)

            self.guardar_en_archivo()
            return True

        return False

    # ======================================================
    # ACTUALIZAR PRODUCTO
    # ======================================================
    def actualizar_producto(self, sku, stock=None, precio_compra=None, precio_venta=None):

        if sku in self.__productos:
            p = self.__productos[sku]

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
    # BUSCAR
    # ======================================================
    def buscar_producto(self, texto):

        texto = texto.lower()

        return [
            p for p in self.__productos.values()
            if texto in p.get_nombre_producto().lower()
        ]

    # ======================================================
    # LISTAR TODOS
    # ======================================================
    def listar_todos(self):
        return list(self.__productos.values())