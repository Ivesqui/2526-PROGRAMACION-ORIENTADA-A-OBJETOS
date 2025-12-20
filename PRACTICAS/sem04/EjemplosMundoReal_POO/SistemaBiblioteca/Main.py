# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

# Importación de clases
from Libro import Libro
from Usuario import Usuario
from Biblioteca import Biblioteca

def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n--- MENÚ BIBLIOTECA ---")
    print("1. Ver libros")
    print("2. Prestar libro")
    print("3. Ver libros prestados")
    print("4. Salir")

def main():
    """
    Función principal del sistema.
    """

    # Crear biblioteca y usuario
    biblioteca = Biblioteca()
    usuario = Usuario("María López")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez"))
    biblioteca.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry"))
    biblioteca.agregar_libro(Libro("Don Quijote de la Mancha", "Miguel de Cervantes"))

    # Bucle del menú
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.mostrar_libros()

        elif opcion == "2":
            biblioteca.mostrar_libros()
            try:
                indice = int(input("Seleccione el libro: ")) - 1
                libro = biblioteca.obtener_libro(indice)

                if libro and libro.prestar():
                    usuario.agregar_libro(libro)
                    print("✅ Libro prestado con éxito.")

            except ValueError:
                print("❌ Entrada inválida.")

        elif opcion == "3":
            usuario.mostrar_libros()

        elif opcion == "4":
            print("👋 Gracias por usar la biblioteca.")
            break

        else:
            print("❌ Opción no válida.")

# Punto de inicio del programa
if __name__ == "__main__":
    main()
