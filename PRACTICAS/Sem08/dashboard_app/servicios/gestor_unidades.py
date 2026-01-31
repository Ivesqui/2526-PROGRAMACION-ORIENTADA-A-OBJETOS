from dashboard_app.data.sistema_archivos import listar_elementos
from dashboard_app.modelos.unidad import Unidad
import os

def obtener_unidades(ruta, solo_unidades=False):
    # Obtiene las carpetas y scripts de la ruta
    carpetas, _ = listar_elementos(ruta)

    # Si se pide solo unidades, filtra las carpetas que empiezan con "unidad"
    if solo_unidades:
        carpetas = [
            c for c in carpetas
            if c.lower().startswith("unidad")
        ]

    # Convierte cada carpeta en un objeto Unidad con su ruta completa
    return [Unidad(c, os.path.join(ruta, c)) for c in carpetas]
