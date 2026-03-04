"""
main.py

Punto de entrada del sistema.
Se encarga de inicializar los componentes y arrancar la aplicación.
No contiene lógica de negocio.
"""

from servicios.biblioteca_servicio import BibliotecaServicio
from interfaz.menu import Menu


def main():
    """
    Función principal del sistema.
    """

    # Se crea la instancia del servicio (lógica del negocio)
    servicio = BibliotecaServicio()

    # Se crea el menú y se le inyecta el servicio
    menu = Menu(servicio)

    # Se ejecuta la interfaz
    menu.ejecutar()


if __name__ == "__main__":
    main()