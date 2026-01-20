"""
Archivo __init__.py del paquete SERVICIOS

Este archivo define la inicialización del paquete 'servicios'.

Se utiliza para agrupar y exponer las clases encargadas de la lógica del sistema,
separando las responsabilidades respecto a los modelos.

Permite acceder a las clases del paquete de manera más limpia desde el programa
principal, por ejemplo:

    from servicios import UsuarioServicio

De esta forma se mantiene una arquitectura organizada basada en el principio
de separación de responsabilidades.
"""

from .usuario_servicio import UsuarioServicio

__all__ = ["UsuarioServicio"]
