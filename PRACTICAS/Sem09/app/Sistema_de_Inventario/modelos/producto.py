class Producto:
    def __init__(self, sku, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Aquí se valida que los datos cumplan reglas básicas de negocio,
        evitando que existan productos inválidos dentro del sistema.
        """

        # Validación: el SKU no puede estar vacío ni contener solo espacios
        if not sku or not sku.strip():
            raise ValueError("El SKU no puede estar vacío")

        # Validación: el nombre del producto es obligatorio
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        # Validación: la cantidad no puede ser negativa
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        # Validación: el precio no puede ser negativo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        # Atributos privados (encapsulamiento)
        self.__sku = sku
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # =========================
    # Getters
    # =========================

    def get_sku(self):
        """Devuelve el SKU del producto"""
        return self.__sku

    def get_nombre(self):
        """Devuelve el nombre del producto"""
        return self.__nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible"""
        return self.__cantidad

    def get_precio(self):
        """Devuelve el precio del producto"""
        return self.__precio

    # =========================
    # Setters con validación
    # =========================

    def set_cantidad(self, cantidad):
        """
        Actualiza la cantidad del producto.
        Se valida que no sea negativa.
        """
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.__cantidad = cantidad

    def set_precio(self, precio):
        """
        Actualiza el precio del producto.
        Se valida que no sea negativo.
        """
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = precio
