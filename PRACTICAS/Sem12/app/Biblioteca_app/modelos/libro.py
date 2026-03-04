"""
modelo/libro.py

Clase Libro mejorada con manejo de estado.
"""

class Libro:
    """
    Representa un libro dentro del sistema.
    """

    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str, anio_publicacion: int):

        # Tupla inmutable (requisito)
        self._info = (titulo, autor)

        self._categoria = categoria
        self._isbn = isbn
        self._anio_publicacion = anio_publicacion

        # Nuevo atributo: estado del libro
        # Estado inicial siempre será "Disponible"
        self._estado = "Disponible"

    # =========================
    # GETTERS
    # =========================

    def obtener_titulo(self):
        return self._info[0]

    def obtener_autor(self):
        return self._info[1]

    def obtener_categoria(self):
        return self._categoria

    def obtener_isbn(self):
        return self._isbn

    def obtener_anio_publicacion(self):
        return self._anio_publicacion

    def obtener_estado(self):
        return self._estado

    # =========================
    # Métodos para cambiar estado
    # =========================

    def prestar(self):
        self._estado = "Prestado"

    def devolver(self):
        self._estado = "Disponible"

    def __str__(self):
        return (
            f"Título: {self.obtener_titulo()} | "
            f"Autor: {self.obtener_autor()} | "
            f"Categoría: {self._categoria} | "
            f"ISBN: {self._isbn} | "
            f"Año: {self._anio_publicacion} | "
            f"Estado: {self._estado}"
        )