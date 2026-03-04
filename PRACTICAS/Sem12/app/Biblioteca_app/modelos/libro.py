"""
modelo/libro.py

Este módulo define la clase Libro.
Representa la entidad Libro dentro del sistema.
NO contiene lógica de negocio.
Solo define estructura y comportamiento propio del objeto.
"""

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """

    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str, anio_publicacion: int):
        """
        Constructor de la clase Libro.

        Requisito técnico:
        - Título y autor deben almacenarse en una TUPLA (inmutable).
        """

        # Tupla inmutable que almacena (titulo, autor)
        self._info = (titulo, autor)

        # Categoría del libro
        self._categoria = categoria

        # ISBN único del libro
        self._isbn = isbn

        # Año de publicación
        self._anio_publicacion = anio_publicacion

    # =========================
    # Métodos GET (Encapsulamiento)
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

    def __str__(self):
        """
        Representación amigable del objeto.
        """
        return (
            f"Título: {self.obtener_titulo()} | "
            f"Autor: {self.obtener_autor()} | "
            f"Categoría: {self._categoria} | "
            f"ISBN: {self._isbn} | "
            f"Año: {self._anio_publicacion}"
        )