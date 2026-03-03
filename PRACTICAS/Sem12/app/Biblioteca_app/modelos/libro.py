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

    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
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

    def __str__(self):
        """
        Representación amigable del objeto.
        """
        return f"Título: {self.obtener_titulo()} | Autor: {self.obtener_autor()} | Categoría: {self._categoria} | ISBN: {self._isbn}"