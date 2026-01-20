"""
Archivo __init__.py del paquete MODELOS

Este archivo permite que la carpeta 'modelos' sea reconocida como un paquete
dentro del proyecto.

Su función principal es centralizar las importaciones de las clases del paquete,
facilitando su uso desde otras capas del sistema, como servicios o main.py.

Gracias a este archivo, se puede importar la clase Usuario de la siguiente forma:

    from modelos import Usuario

en lugar de utilizar rutas más largas como:

    from modelos.usuario import Usuario

Esto mejora la organización, legibilidad y mantenimiento del código.
"""

from .usuario import Usuario

__all__ = ["Usuario"]
