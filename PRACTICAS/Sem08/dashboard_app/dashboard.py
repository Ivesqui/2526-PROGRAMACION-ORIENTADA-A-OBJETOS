# Importa el módulo os para interactuar con el sistema operativo
# Se utiliza para limpiar la consola, manejar rutas y ejecutar scripts
import os

# Importa la función que obtiene carpetas (unidades) desde la capa de servicios
from dashboard_app.servicios.gestor_unidades import obtener_unidades

# Importa la función que obtiene scripts Python desde la capa de servicios
from dashboard_app.servicios.gestor_scripts import obtener_scripts

# Importa funciones de la interfaz de usuario (menús y encabezado)
from dashboard_app.ui.menus import (
    mostrar_encabezado,
    menu_unidades,
    menu_scripts
)


def iniciar_dashboard(ruta_base):
    """
    Función principal del sistema.
    Muestra el menú inicial del dashboard y permite seleccionar
    una unidad para explorar su contenido.

    :param ruta_base: ruta raíz donde se encuentran las unidades
    """

    # Bucle principal del dashboard
    while True:
        # Limpia la consola según el sistema operativo
        os.system("cls" if os.name == "nt" else "clear")

        # Muestra el encabezado del sistema
        mostrar_encabezado()

        # Obtiene únicamente las carpetas que representan unidades
        # (por ejemplo: UNIDAD 1, UNIDAD 2, etc.)
        unidades = obtener_unidades(ruta_base, solo_unidades=True)

        # Muestra el menú con las unidades encontradas
        menu_unidades(unidades)

        # Solicita al usuario que seleccione una unidad
        opcion = input("\nSeleccione una unidad: ")

        # Opción para salir del sistema
        if opcion == "0":
            break

        try:
            # Convierte la opción a índice y obtiene la unidad seleccionada
            unidad = unidades[int(opcion) - 1]

            # Llama a la función para explorar el contenido de la unidad
            explorar_unidad(unidad.ruta)

        except:
            # Manejo básico de error si la opción es inválida
            input("Opción inválida...")


def explorar_unidad(ruta_actual):
    """
    Permite explorar el contenido de una carpeta seleccionada.
    Muestra subcarpetas y scripts Python, y permite navegar o ejecutar scripts.

    :param ruta_actual: ruta de la carpeta que se está explorando
    """

    # Bucle para permanecer dentro de la unidad actual
    while True:
        # Limpia la consola
        os.system("cls" if os.name == "nt" else "clear")

        # Muestra el nombre de la carpeta actual
        print(f"--- {os.path.basename(ruta_actual)} ---\n")

        # Obtiene todas las subcarpetas (sin filtrar por nombre)
        carpetas = obtener_unidades(ruta_actual)

        # Obtiene los scripts Python (.py) de la carpeta actual
        scripts = obtener_scripts(ruta_actual)

        # Muestra las carpetas disponibles
        print("Carpetas:")
        menu_unidades(carpetas)

        # Muestra los scripts disponibles
        print("\nScripts:")
        menu_scripts(scripts)

        # Solicita una opción al usuario
        opcion = input("\nSeleccione una opción: ")

        # Opción para regresar al menú anterior
        if opcion == "0":
            break

        try:
            # Convierte la opción ingresada a entero
            opcion = int(opcion)

            # Si la opción corresponde a una carpeta
            if opcion <= len(carpetas):
                carpeta = carpetas[opcion - 1]

                # Navega recursivamente dentro de la subcarpeta
                explorar_unidad(carpeta.ruta)

            else:
                # Calcula el índice real del script seleccionado
                index_script = opcion - len(carpetas) - 1
                script = scripts[index_script]

                # Ejecuta el script seleccionado
                ejecutar_script(os.path.join(ruta_actual, script))

        except:
            # Manejo de error para entradas inválidas
            input("Opción inválida...")


def ejecutar_script(ruta_script):
    """
    Ejecuta un script Python seleccionado por el usuario.

    :param ruta_script: ruta completa del archivo .py a ejecutar
    """

    # Muestra qué script se va a ejecutar
    print(f"\nEjecutando: {ruta_script}")

    # Ejecuta el script usando el intérprete de Python
    os.system(f'python "{ruta_script}"')

    # Pausa la ejecución hasta que el usuario presione Enter
    input("\nPresione Enter para continuar...")
