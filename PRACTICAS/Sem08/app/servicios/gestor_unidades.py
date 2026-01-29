import os
from app.data.file_system import listar_carpetas
from app.modelos.unidad import Unidad


def obtener_unidades(ruta_base):
    carpetas = listar_carpetas(ruta_base)
    unidades = []

    for carpeta in carpetas:
        if carpeta.lower().startswith("unidad"):
            ruta = os.path.join(ruta_base, carpeta)
            unidades.append(Unidad(carpeta, ruta))

    return unidades
