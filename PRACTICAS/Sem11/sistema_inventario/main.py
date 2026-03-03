# ======================================================
# IMPORTACIÓN
# ======================================================

# Se importa la función ejecutar_menu desde el módulo interfaz.menu.
# Esta función contiene toda la lógica del sistema de inventarios
# y controla el flujo principal del programa.
from interfaz.menu import ejecutar_menu


# ======================================================
# FUNCIÓN PRINCIPAL
# ======================================================
def main():
    """
    Función principal del programa.

    Su única responsabilidad es llamar a la función
    ejecutar_menu(), que inicia el sistema.
    """
    ejecutar_menu()


# ======================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ======================================================
if __name__ == "__main__":
    """
    Esta condición verifica si el archivo está siendo
    ejecutado directamente (y no importado como módulo).

    Si se ejecuta directamente, se llama a la función main(),
    iniciando así la aplicación.
    """
    main()
