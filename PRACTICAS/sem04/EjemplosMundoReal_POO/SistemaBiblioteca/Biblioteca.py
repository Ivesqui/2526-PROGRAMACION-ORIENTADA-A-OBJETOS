# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

class Biblioteca:
    """
    Clase Biblioteca
    Gestiona los libros disponibles.
    """

    def __init__(self):
        # Lista de libros de la biblioteca
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca.
        """
        self.libros.append(libro)

    def mostrar_libros(self):
        """
        Muestra todos los libros de la biblioteca.
        """
        print("\n📚 Libros en la biblioteca:")
        for i, libro in enumerate(self.libros, start=1):
            print(f"{i}. ", end="")
            libro.mostrar_info()

    def obtener_libro(self, indice):
        """
        Devuelve un libro según el índice ingresado.
        """
        if 0 <= indice < len(self.libros):
            return self.libros[indice]
        else:
            print("❌ Libro no válido.")
            return None
