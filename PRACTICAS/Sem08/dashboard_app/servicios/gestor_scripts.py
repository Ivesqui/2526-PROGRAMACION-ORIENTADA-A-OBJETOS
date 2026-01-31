from dashboard_app.data.file_system import listar_elementos
import os

def obtener_scripts(ruta):
    # Obtiene solo los scripts (.py) de la ruta indicada
    _, scripts = listar_elementos(ruta)
    return scripts
