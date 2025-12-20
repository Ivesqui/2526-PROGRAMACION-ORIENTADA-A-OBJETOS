# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

class Usuario:
    """
    Clase Usuario
    Representa a un usuario de la biblioteca.
    """

    def __init__(self, nombre):
        # Nombre del usuario
        self.nombre = nombre

        # Lista de libros prestados
        self.libros_prestados = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la lista de libros prestados.
        """
        self.libros_prestados.append(libro)

    def mostrar_libros(self):
        """
        Muestra los libros que el usuario ha prestado.
        """
        print(f"\n📖 Libros prestados a {self.nombre}:")
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(f"- {libro.titulo}")
