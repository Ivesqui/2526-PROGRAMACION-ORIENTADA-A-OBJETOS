import os
import subprocess


def limpiar_pantalla():
    # Limpia la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            limpiar_pantalla()
            print(f"--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems (Linux/macOS)
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    while True:
        limpiar_pantalla()
        print("==========================================================")
        print("     SISTEMA DE GESTIÓN DE PROYECTOS - POO")
        print("==========================================================")
        print(f" Estudiante: Christian Iván Estupiñán Quintero")
        print(f" Carrera: Tecnologías de la Información - 2do Nivel (A)")
        print(f" Docente: Mgs. Kevin Bolivar Lascano Sanchez")
        print("----------------------------------------------------------")
        print("              MENÚ PRINCIPAL - UNIDADES")
        print("----------------------------------------------------------")

        # Mejora: Detección automática de carpetas de Unidades
        unidades = [f.name for f in os.scandir(ruta_base) if f.is_dir() and f.name.lower().startswith('unidad')]
        unidades.sort()  # Ordenar para que aparezca Unidad 1, 2, etc.

        for i, unidad in enumerate(unidades, start=1):
            print(f"{i} - {unidad}")

        print("0 - Salir")
        print("----------------------------------------------------------")

        eleccion = input("Selecciona una unidad para ver sus tareas o '0' para salir: ")
        if eleccion == '0':
            print("Finalizando Dashboard. ¡Éxito en tus estudios, Christian!")
            break

        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(unidades):
                mostrar_sub_menu(os.path.join(ruta_base, unidades[indice]))
            else:
                print("Opción no válida.")
                input("Presiona Enter para continuar...")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            input("Presiona Enter para continuar...")


def mostrar_sub_menu(ruta_unidad):
    while True:
        limpiar_pantalla()
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        print(f"--- Explorando: {os.path.basename(ruta_unidad)} ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion = input("\nSelecciona una subcarpeta o '0' para regresar: ")
        if eleccion == '0':
            break

        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada no válida.")


def mostrar_scripts(ruta_sub_carpeta):
    while True:
        limpiar_pantalla()
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

        print(f"--- Scripts en: {os.path.basename(ruta_sub_carpeta)} ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")
        print("9 - Menú Principal")

        eleccion = input("\nSelecciona un script para ver/ejecutar: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return "principal"

        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input("\n¿Deseas ejecutar este script? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    input("\nPresiona Enter para volver...")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada no válida.")


if __name__ == "__main__":
    mostrar_menu()
