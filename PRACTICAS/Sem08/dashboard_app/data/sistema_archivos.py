import os  # Permite interactuar con el sistema de archivos

def listar_elementos(ruta):
    carpetas = []  # Guarda los nombres de las carpetas
    scripts = []   # Guarda los archivos .py

    # Recorre los elementos de la ruta indicada
    for f in os.scandir(ruta):
        if f.is_dir():
            carpetas.append(f.name)
        elif f.is_file() and f.name.endswith(".py"):
            scripts.append(f.name)

    # Devuelve carpetas y scripts encontrados
    return carpetas, scripts