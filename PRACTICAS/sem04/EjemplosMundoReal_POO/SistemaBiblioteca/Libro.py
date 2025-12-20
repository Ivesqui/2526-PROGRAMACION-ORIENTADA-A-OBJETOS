# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

class Libro:
    """
    Clase Libro
    Representa un libro disponible en la biblioteca.
    """

    def __init__(self, titulo, autor):
        # Título del libro
        self.titulo = titulo

        # Autor del libro
        self.autor = autor

        # Estado del libro (True = disponible, False = prestado)
        self.disponible = True

    def mostrar_info(self):
        """
        Muestra la información del libro.
        """
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"{self.titulo} - {self.autor} | Estado: {estado}")

    def prestar(self):
        """
        Marca el libro como prestado si está disponible.
        """
        if self.disponible:
            self.disponible = False
            return True
        else:
            print("❌ El libro no está disponible.")
            return False
