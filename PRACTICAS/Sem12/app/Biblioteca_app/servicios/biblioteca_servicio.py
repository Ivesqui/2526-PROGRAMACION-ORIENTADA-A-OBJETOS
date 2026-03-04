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

    def __init__(self):
        # Ahora tenemos un catálogo general
        self._catalogo = {}

        self._usuarios = {}
        self._ids_usuarios = set()

    # =========================
    # Gestión de Libros
    # =========================

    def anadir_libro(self, titulo, autor, categoria, isbn, anio_publicacion):
        if isbn in self._catalogo:
            return "El libro ya existe."

        libro = Libro(titulo, autor, categoria, isbn, anio_publicacion)
        self._catalogo[isbn] = libro
        return "Libro añadido correctamente."

    def quitar_libro(self, isbn):
        if isbn in self._catalogo:
            if self._catalogo[isbn].obtener_estado() == "Prestado":
                return "No se puede eliminar un libro prestado."
            del self._catalogo[isbn]
            return "Libro eliminado."
        return "Libro no encontrado."

    # =========================
    # Usuarios
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

        if isbn not in self._catalogo:
            return "Libro no encontrado."

        libro = self._catalogo[isbn]

        if libro.obtener_estado() == "Prestado":
            return "El libro ya está prestado."

        usuario = self._usuarios[user_id]

        libro.prestar()
        usuario.agregar_libro(libro)

        return "Préstamo realizado con éxito."

    def devolver_libro(self, user_id, isbn):
        if user_id not in self._usuarios:
            return "Usuario no encontrado."

        usuario = self._usuarios[user_id]
        libro = usuario.devolver_libro(isbn)

        if libro:
            libro.devolver()
            return "Libro devuelto correctamente."

        return "El usuario no tiene ese libro."

    # =========================
    # Búsquedas (ahora parciales)
    # =========================

    def buscar_por_titulo(self, titulo):
        titulo = titulo.lower()

        return [
            libro for libro in self._catalogo.values()
            if titulo in libro.obtener_titulo().lower()
        ]

    def buscar_por_autor(self, autor):
        autor = autor.lower()

        return [
            libro for libro in self._catalogo.values()
            if autor in libro.obtener_autor().lower()
        ]

    def buscar_por_categoria(self, categoria):
        categoria = categoria.lower()

        return [
            libro for libro in self._catalogo.values()
            if categoria in libro.obtener_categoria().lower()
        ]

    def buscar_por_anio(self, anio):
        return [
            libro for libro in self._catalogo.values()
            if libro.obtener_anio_publicacion() == anio
        ]

    def listar_libros_usuario(self, user_id):
        if user_id not in self._usuarios:
            return []

        return self._usuarios[user_id].obtener_libros_prestados()