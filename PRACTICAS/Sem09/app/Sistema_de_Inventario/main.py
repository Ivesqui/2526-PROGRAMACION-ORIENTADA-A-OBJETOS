from database.conexion import crear_tabla
from interfaz.menu import ejecutar_menu

def main():
    crear_tabla()     # Inicializa la base de datos
    ejecutar_menu()   # Muestra el menú

if __name__ == "__main__":
    main()