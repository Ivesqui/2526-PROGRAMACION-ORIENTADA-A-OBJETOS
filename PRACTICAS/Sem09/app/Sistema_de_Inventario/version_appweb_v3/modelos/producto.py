class Producto:
    """
    Representa un producto del inventario.
    Contiene únicamente reglas de negocio.
    No tiene conocimiento de base de datos.
    """

    def __init__(
            self,
            sku: str,
            nombre_producto: str,
            categoria: str,
            unidad: str,
            precio_compra: float,
            precio_venta: float,
            stock_actual: int,
            stock_minimo: int,
            activo: bool = True,
            codigo_barras: str = None
    ):
        # -------------------------
        # Validaciones de negocio
        # -------------------------
        if not sku or not sku.strip():
            raise ValueError("El SKU no puede estar vacío")

        if not nombre_producto or not nombre_producto.strip():
            raise ValueError("El nombre del producto no puede estar vacío")

        if precio_compra < 0:
            raise ValueError("El precio de compra no puede ser negativo")

        if precio_venta < precio_compra:
            raise ValueError("El precio de venta no puede ser menor al de compra")

        if stock_actual < 0:
            raise ValueError("El stock no puede ser negativo")

        if stock_minimo < 0:
            raise ValueError("El stock mínimo no puede ser negativo")

        # -------------------------
        # Atributos privados
        # -------------------------
        self.__sku = sku
        self.__nombre_producto = nombre_producto
        self.__categoria = categoria
        self.__unidad = unidad
        self.__precio_compra = precio_compra
        self.__precio_venta = precio_venta
        self.__stock_actual = stock_actual
        self.__stock_minimo = stock_minimo
        self.__activo = activo
        self.__codigo_barras = codigo_barras

    # -------------------------
    # Getters
    # -------------------------
    def get_sku(self):
        return self.__sku

    def get_nombre_producto(self):
        return self.__nombre_producto

    def get_categoria(self):
        return self.__categoria

    def get_unidad(self):
        return self.__unidad

    def get_precio_compra(self):
        return self.__precio_compra

    def get_precio_venta(self):
        return self.__precio_venta

    def get_stock_actual(self):
        return self.__stock_actual

    def get_stock_minimo(self):
        return self.__stock_minimo

    def esta_activo(self):
        return self.__activo

    def get_codigo_barras(self):
        return self.__codigo_barras