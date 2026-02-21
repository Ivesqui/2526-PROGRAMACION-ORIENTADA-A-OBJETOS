class Producto:
    """
    Entidad de Negocio: Producto
    Aplica el principio de Encapsulamiento y validaciones de integridad.
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
        self.__validar(sku, nombre_producto, precio_compra, precio_venta, stock_actual, stock_minimo)

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

    def __validar(self, sku, nombre, p_compra, p_venta, stock, stock_min):
        if not sku or not sku.strip():
            raise ValueError("El SKU no puede estar vacío")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if p_compra < 0:
            raise ValueError("El precio de compra no puede ser negativo")
        if p_venta < p_compra:
            raise ValueError("El precio de venta no puede ser menor al de compra")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

    # -------------------------
    # Getters (Uso de Decoradores @property)
    # -------------------------
    # En Python Senior, usamos @property en lugar de get_xxx()
    # para que se acceda como p.sku en lugar de p.get_sku()

    @property
    def sku(self):
        return self.__sku

    @property
    def nombre(self):
        return self.__nombre_producto

    @property
    def stock(self):
        return self.__stock_actual

    @property
    def activo(self):
        return self.__activo

    @property
    def precio_venta(self):
        return self.__precio_venta

    @property
    def precio_compra(self):
        return self.__precio_compra

    @property
    def stock_minimo(self):
        return self.__stock_minimo

    # -------------------------
    # Métodos de utilidad de negocio
    # -------------------------
    def to_dict(self):
        """Convierte la entidad a un diccionario para la API (JSON)"""
        return {
            "sku": self.__sku,
            "nombre": self.__nombre_producto,
            "categoria": self.__categoria,
            "stock": self.__stock_actual,
            "precio_venta": self.__precio_venta,
            "es_bajo_stock": self.__stock_actual <= self.__stock_minimo
        }