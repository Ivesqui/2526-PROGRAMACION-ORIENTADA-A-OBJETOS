"""
servicios/biblioteca_servicio.py

Contiene la lógica del negocio.
Administra libros, usuarios, préstamos y búsquedas.

Aquí se evidencia la separación de capas:
- Modelos: solo representan entidades
- Servicios: gestionan la lógica
"""

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Clase que gestiona la biblioteca.
    """

    def __init__(self):
        # Diccionario requerido:
        # Clave: ISBN
        # Valor: Objeto Libro
        self._libros_disponibles = {}

        # Diccionario para almacenar usuarios
        self._usuarios = {}

        # Set requerido para garantizar IDs únicos
        self._ids_usuarios = set()

    # =========================
    # Gestión de Libros
    # =========================

    def anadir_libro(self, titulo, autor, categoria, isbn, anio_publicacion):
        if isbn in self._libros_disponibles:
            return "El libro ya existe."

        # Se pasa ahora el año al constructor
        libro = Libro(titulo, autor, categoria, isbn, anio_publicacion)
        self._libros_disponibles[isbn] = libro
        return "Libro añadido correctamente."

    def quitar_libro(self, isbn):
        if isbn in self._libros_disponibles:
            del self._libros_disponibles[isbn]
            return "Libro eliminado."
        return "Libro no encontrado."

    # =========================
    # Gestión de Usuarios
    # =========================

    def registrar_usuario(self, nombre, user_id):
        if user_id in self._ids_usuarios:
            return "ID ya registrado."

        usuario = Usuario(nombre, user_id)
        self._usuarios[user_id] = usuario
        self._ids_usuarios.add(user_id)
        return "Usuario registrado correctamente."

    def dar_baja_usuario(self, user_id):
        if user_id in self._usuarios:
            del self._usuarios[user_id]
            self._ids_usuarios.remove(user_id)
            return "Usuario eliminado."
        return "Usuario no encontrado."

    # =========================
    # Préstamos
    # =========================

    def prestar_libro(self, user_id, isbn):
        if user_id not in self._usuarios:
            return "Usuario no encontrado."

        if isbn not in self._libros_disponibles:
            return "Libro no disponible."

        usuario = self._usuarios[user_id]
        libro = self._libros_disponibles.pop(isbn)

        usuario.agregar_libro(libro)
        return "Préstamo realizado con éxito."

    def devolver_libro(self, user_id, isbn):
        if user_id not in self._usuarios:
            return "Usuario no encontrado."

        usuario = self._usuarios[user_id]
        libro = usuario.devolver_libro(isbn)

        if libro:
            self._libros_disponibles[isbn] = libro
            return "Libro devuelto correctamente."
        return "El usuario no tiene ese libro."

    # =========================
    # Búsquedas
    # =========================

    def buscar_por_titulo(self, titulo):
        return [
            libro for libro in self._libros_disponibles.values()
            if libro.obtener_titulo().lower() == titulo.lower()
        ]

    def buscar_por_autor(self, autor):
        return [
            libro for libro in self._libros_disponibles.values()
            if libro.obtener_autor().lower() == autor.lower()
        ]

    def buscar_por_categoria(self, categoria):
        return [
            libro for libro in self._libros_disponibles.values()
            if libro.obtener_categoria().lower() == categoria.lower()
        ]

    def listar_libros_usuario(self, user_id):
        if user_id not in self._usuarios:
            return []

        return self._usuarios[user_id].obtener_libros_prestados()