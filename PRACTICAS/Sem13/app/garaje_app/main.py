import tkinter as tk
from ui.app_tkinter import AppGaraje


def main():
    """
    Función principal que inicia la aplicación.
    """
    # Crear ventana principal
    root = tk.Tk()

    # Crear aplicación
    app = AppGaraje(root)

    # Iniciar loop de eventos
    root.mainloop()


if __name__ == "__main__":
    main()