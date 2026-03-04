"""
interfaz/menu.py

Este módulo representa la capa de presentación.
Aquí solo se gestiona la interacción con el usuario.
NO contiene lógica de negocio.
"""

class Menu:
    """
    Clase que maneja el menú interactivo.
    """

    def __init__(self, servicio):
        """
        Recibe una instancia de BibliotecaServicio.
        Esto permite desacoplar la interfaz de la lógica.
        """
        self._servicio = servicio

    def mostrar_menu(self):
        print("\n===== BIBLIOTECA DIGITAL =====")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar por título")
        print("8. Buscar por autor")
        print("9. Buscar por categoría")
        print("10. Buscar por año")
        print("11. Listar libros de usuario")
        print("12. Salir")

    def ejecutar(self):
        """
        Ejecuta el ciclo principal del menú.
        """

        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoría: ")
                isbn = input("ISBN: ")

                # Nuevo campo: año de publicación
                try:
                    anio_publicacion = int(input("Año de publicación: "))
                except ValueError:
                    print("El año debe ser un número válido.")
                    continue

                print(self._servicio.anadir_libro(
                    titulo, autor, categoria, isbn, anio_publicacion
                ))

            elif opcion == "2":
                isbn = input("ISBN del libro a eliminar: ")
                print(self._servicio.quitar_libro(isbn))

            elif opcion == "3":
                nombre = input("Nombre: ")
                user_id = input("ID usuario: ")
                print(self._servicio.registrar_usuario(nombre, user_id))

            elif opcion == "4":
                user_id = input("ID usuario: ")
                print(self._servicio.dar_baja_usuario(user_id))

            elif opcion == "5":
                user_id = input("ID usuario: ")
                isbn = input("ISBN libro: ")
                print(self._servicio.prestar_libro(user_id, isbn))

            elif opcion == "6":
                user_id = input("ID usuario: ")
                isbn = input("ISBN libro: ")
                print(self._servicio.devolver_libro(user_id, isbn))

            elif opcion == "7":
                titulo = input("Título: ")
                resultados = self._servicio.buscar_por_titulo(titulo)

                if resultados:
                    for libro in resultados:
                        print(libro)
                else:
                    print("No se encontraron resultados.")

            elif opcion == "8":
                autor = input("Autor: ")
                resultados = self._servicio.buscar_por_autor(autor)

                if resultados:
                    for libro in resultados:
                        print(libro)
                else:
                    print("No se encontraron resultados.")

            elif opcion == "9":
                categoria = input("Categoría: ")
                resultados = self._servicio.buscar_por_categoria(categoria)

                if resultados:
                    for libro in resultados:
                        print(libro)
                else:
                    print("No se encontraron resultados.")


            elif opcion == "10":

                try:
                    anio = int(input("Año de publicación: "))

                except ValueError:
                    print("Debe ingresar un año válido.")
                    continue
                resultados = self._servicio.buscar_por_anio(anio)

                if resultados:
                    for libro in resultados:
                        print(libro)
                else:
                    print("No se encontraron resultados.")


            elif opcion == "11":
                user_id = input("ID usuario: ")
                libros = self._servicio.listar_libros_usuario(user_id)

                if libros:
                    for libro in libros:
                        print(libro)

                else:
                    print("El usuario no tiene libros o no existe.")

            elif opcion == "12":
                print("Saliendo del sistema...")
                break