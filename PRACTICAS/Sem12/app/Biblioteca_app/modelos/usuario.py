"""
modelo/usuario.py

Define la clase Usuario.
Representa la entidad Usuario.
No contiene lógica de negocio.
"""

class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    """

    def __init__(self, nombre: str, user_id: str):
        """
        Constructor de la clase Usuario.

        Requisito técnico:
        - Los libros prestados deben almacenarse en una LISTA.
        """

        self._nombre = nombre
        self._user_id = user_id

        # Lista que almacena objetos Libro prestados
        self._libros_prestados = []

    # =========================
    # Métodos GET
    # =========================

    def obtener_nombre(self):
        return self._nombre

    def obtener_id(self):
        return self._user_id

    def obtener_libros_prestados(self):
        return self._libros_prestados

    # =========================
    # Métodos internos del modelo
    # =========================

    def agregar_libro(self, libro):
        """
        Agrega un libro a la lista de préstamos.
        """
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        """
        Elimina un libro de la lista de préstamos según su ISBN.
        """
        for libro in self._libros_prestados:
            if libro.obtener_isbn() == isbn:
                self._libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self._nombre} | ID: {self._user_id}"