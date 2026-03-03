# ======================================================
# CLASE PRODUCTO
# ======================================================

class Producto:
    """
    Representa un producto dentro del inventario.

    Esta clase contiene únicamente reglas de negocio,
    es decir, validaciones y comportamiento propio del producto.

    No tiene responsabilidad sobre almacenamiento,
    base de datos o archivos.
    """

    # ======================================================
    # CONSTRUCTOR
    # ======================================================
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
        activo: bool = True
    ):
        """
        Inicializa un objeto Producto con sus atributos.

        Incluye validaciones de negocio para garantizar
        que el objeto se cree en un estado válido.
        """

        # -------------------------
        # VALIDACIONES DE NEGOCIO
        # -------------------------

        # El SKU no puede estar vacío ni contener solo espacios
        if not sku or not sku.strip():
            raise ValueError("El SKU no puede estar vacío")

        # El nombre del producto no puede estar vacío
        if not nombre_producto or not nombre_producto.strip():
            raise ValueError("El nombre del producto no puede estar vacío")

        # El precio de compra no puede ser negativo
        if precio_compra < 0:
            raise ValueError("El precio de compra no puede ser negativo")

        # El precio de venta no puede ser menor que el precio de compra
        if precio_venta < precio_compra:
            raise ValueError("El precio de venta no puede ser menor al de compra")

        # El stock actual no puede ser negativo
        if stock_actual < 0:
            raise ValueError("El stock no puede ser negativo")

        # El stock mínimo no puede ser negativo
        if stock_minimo < 0:
            raise ValueError("El stock mínimo no puede ser negativo")

        # -------------------------
        # ATRIBUTOS PRIVADOS
        # -------------------------
        # Se usan atributos privados para aplicar encapsulamiento,
        # evitando modificaciones directas desde fuera de la clase.

        self.__sku = sku
        self.__nombre_producto = nombre_producto
        self.__categoria = categoria
        self.__unidad = unidad
        self.__precio_compra = precio_compra
        self.__precio_venta = precio_venta
        self.__stock_actual = stock_actual
        self.__stock_minimo = stock_minimo
        self.__activo = activo


    # ======================================================
    # MÉTODOS GETTERS
    # ======================================================
    # Permiten acceder a los atributos privados de forma controlada.

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
        """
        Retorna True si el producto está activo,
        o False si ha sido desactivado.
        """
        return self.__activo


    # ======================================================
    # MÉTODOS SETTERS CONTROLADOS
    # ======================================================
    # Permiten modificar atributos aplicando validaciones.

    def set_stock_actual(self, nuevo_stock):
        """
        Modifica el stock actual del producto.

        Valida que el nuevo stock no sea negativo.
        """
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.__stock_actual = nuevo_stock


    def set_precio_compra(self, nuevo_precio):
        """
        Modifica el precio de compra.

        Valida que no sea negativo.
        """
        if nuevo_precio < 0:
            raise ValueError("El precio de compra no puede ser negativo")

        self.__precio_compra = nuevo_precio


    def set_precio_venta(self, nuevo_precio):
        """
        Modifica el precio de venta.

        Valida que no sea menor al precio de compra.
        """
        if nuevo_precio < self.__precio_compra:
            raise ValueError("El precio de venta no puede ser menor al de compra")

        self.__precio_venta = nuevo_precio


    # ======================================================
    # MÉTODOS DE COMPORTAMIENTO
    # ======================================================

    def desactivar(self):
        """
        Cambia el estado del producto a inactivo.

        No elimina el producto del sistema,
        solo lo marca como desactivado.
        """
        self.__activo = False