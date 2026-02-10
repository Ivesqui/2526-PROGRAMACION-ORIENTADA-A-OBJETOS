class Producto:
    """
    Representa un producto del inventario.

    Esta clase NO maneja base de datos.
    Solo representa reglas de negocio.
    """

    def __init__(self, sku, nombre, cantidad, precio, stock_minimo=5):
        if not sku or not sku.strip():
            raise ValueError("El SKU no puede estar vacío")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        if stock_minimo < 0:
            raise ValueError("El stock mínimo no puede ser negativo")

        self.__sku = sku
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        self.__stock_minimo = stock_minimo

    # Getters
    def get_sku(self): return self.__sku
    def get_nombre(self): return self.__nombre
    def get_cantidad(self): return self.__cantidad
    def get_precio(self): return self.__precio
    def get_stock_minimo(self): return self.__stock_minimo

