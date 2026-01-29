import os


def listar_carpetas(ruta):
    return [f.name for f in os.scandir(ruta) if f.is_dir()]


def listar_scripts(ruta):
    return [f.name for f in os.scandir(ruta) if f.is_file() and f.name.endswith(".py")]
