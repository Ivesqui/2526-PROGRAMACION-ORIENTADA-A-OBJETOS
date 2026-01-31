def mostrar_encabezado():
    # Muestra el título principal del sistema en consola
    print("======================================")
    print(" SISTEMA DE GESTIÓN DE PROYECTOS - POO")
    print("======================================\n")


def menu_unidades(unidades):
    # Muestra el menú de unidades disponibles
    for i, u in enumerate(unidades, 1):
        print(f"{i}. {u.nombre}")
    print("0. Salir")  # Opción para salir del sistema


def menu_scripts(scripts):
    # Muestra el menú de scripts dentro de una unidad
    for i, s in enumerate(scripts, 1):
        print(f"{i}. {s}")
    print("0. Regresar")  # Opción para volver al menú anterior
