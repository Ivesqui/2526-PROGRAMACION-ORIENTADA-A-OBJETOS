# ======================================================
# IMPORTACIONES
# ======================================================

# Se importa la clase Producto
from modelos.producto import Producto

# Se importa el módulo json para serialización estructurada
import json


# ======================================================
# CLASE INVENTARIO
# ======================================================
class Inventario:
    """
    Clase encargada de gestionar el inventario.

    Implementa:
    - Diccionario para almacenamiento principal.
    - Conjunto (set) para control de IDs únicos.
    - Listas para resultados filtrados.
    - Persistencia mediante JSON.
    """

    # ======================================================
    # CONSTRUCTOR
    # ======================================================
    def __init__(self):
        """
        Inicializa:
        - Archivo JSON de almacenamiento.
        - Diccionario de productos.
        - Set de SKUs únicos.
        - Carga automática desde archivo.
        """
        self.__archivo = "inventario.json"

        # Diccionario principal:
        # clave = SKU
        # valor = objeto Producto
        self.__productos = {}

        # Set para control eficiente de SKUs únicos
        self.__skus = set()

        # Carga datos al iniciar
        self.cargar_desde_archivo()


    # ======================================================
    # SERIALIZACIÓN A DICCIONARIO
    # ======================================================
    def __producto_a_dict(self, producto):
        """
        Convierte un objeto Producto a diccionario
        para poder guardarlo en formato JSON.
        """
        return {
            "sku": producto.get_sku(),
            "nombre_producto": producto.get_nombre_producto(),
            "categoria": producto.get_categoria(),
            "unidad": producto.get_unidad(),
            "precio_compra": producto.get_precio_compra(),
            "precio_venta": producto.get_precio_venta(),
            "stock_actual": producto.get_stock_actual(),
            "stock_minimo": producto.get_stock_minimo(),
            "activo": producto.esta_activo()
        }


    # ======================================================
    # DESERIALIZACIÓN DESDE DICCIONARIO
    # ======================================================
    def __dict_a_producto(self, datos):
        """
        Convierte un diccionario cargado desde JSON
        nuevamente en un objeto Producto.
        """
        return Producto(
            sku=datos["sku"],
            nombre_producto=datos["nombre_producto"],
            categoria=datos["categoria"],
            unidad=datos["unidad"],
            precio_compra=datos["precio_compra"],
            precio_venta=datos["precio_venta"],
            stock_actual=datos["stock_actual"],
            stock_minimo=datos["stock_minimo"],
            activo=datos["activo"]
        )


    # ======================================================
    # CARGAR DESDE ARCHIVO JSON
    # ======================================================
    def cargar_desde_archivo(self):
        """
        Lee el archivo JSON y reconstruye
        el inventario en memoria.
        """

        self.__productos.clear()
        self.__skus.clear()

        try:
            with open(self.__archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

                for item in datos:
                    producto = self.__dict_a_producto(item)

                    self.__productos[producto.get_sku()] = producto
                    self.__skus.add(producto.get_sku())

        except FileNotFoundError:
            # Si no existe el archivo, lo crea vacío
            with open(self.__archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo)

        except Exception as e:
            print("Error al cargar archivo:", e)


    # ======================================================
    # GUARDAR EN ARCHIVO JSON
    # ======================================================
    def guardar_en_archivo(self):
        """
        Serializa el inventario completo
        y lo guarda en formato JSON.
        """

        try:
            with open(self.__archivo, "w", encoding="utf-8") as archivo:

                # Lista de productos serializados
                lista_productos = [
                    self.__producto_a_dict(p)
                    for p in self.__productos.values()
                ]

                json.dump(lista_productos, archivo, indent=4)

        except Exception as e:
            print("Error al guardar archivo:", e)


    # ======================================================
    # AGREGAR PRODUCTO
    # ======================================================
    def agregar_producto(self, producto: Producto):
        """
        Agrega un nuevo producto.

        Utiliza el set para verificar
        unicidad del SKU.
        """

        if producto.get_sku() in self.__skus:
            return False

        self.__productos[producto.get_sku()] = producto
        self.__skus.add(producto.get_sku())

        self.guardar_en_archivo()
        return True


    # ======================================================
    # ELIMINACIÓN FÍSICA DEL PRODUCTO
    # ======================================================
    def eliminar_producto(self, sku):
        """
        Elimina completamente un producto
        del inventario.
        """

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
    # BUSCAR PRODUCTOS POR NOMBRE
    # ======================================================
    def buscar_producto(self, texto):
        """
        Retorna una lista de productos
        que coincidan con el texto.
        """

        texto = texto.lower()

        return [
            p for p in self.__productos.values()
            if texto in p.get_nombre_producto().lower()
        ]


    # ======================================================
    # LISTAR TODOS LOS PRODUCTOS
    # ======================================================
    def listar_todos(self):
        """
        Retorna una lista con todos los productos.
        """

        return list(self.__productos.values())