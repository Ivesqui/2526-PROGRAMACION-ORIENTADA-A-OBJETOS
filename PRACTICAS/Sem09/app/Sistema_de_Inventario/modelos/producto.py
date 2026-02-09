class Producto:
    """
    Clase que representa un producto del inventario.

    Se usa Programación Orientada a Objetos para:
    - Encapsular los datos del producto
    - Controlar el acceso a los atributos
    - Facilitar mantenimiento y escalabilidad
    """

    def __init__(self, sku, nombre, cantidad, precio):
        # Atributos privados (encapsulación)
        # Se usa doble guion bajo (__)
        # para evitar acceso directo desde fuera de la clase
        self.__sku = sku          # Código único del producto
        self.__nombre = nombre    # Nombre del producto
        self.__cantidad = cantidad  # Stock disponible
        self.__precio = precio    # Precio unitario

    # ======================
    # GETTERS
    # ======================
    # Permiten leer los valores de los atributos privados
    # sin acceder directamente a ellos

    def get_sku(self):
        return self.__sku

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ======================
    # SETTERS
    # ======================
    # Permiten modificar SOLO ciertos atributos
    # No se permite cambiar el SKU ni el nombre
    # porque identifican al producto

    def set_cantidad(self, cantidad):
        # Se separa la lógica de modificación
        # para poder validar datos en el futuro
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio
