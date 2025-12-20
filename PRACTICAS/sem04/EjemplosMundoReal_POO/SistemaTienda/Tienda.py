# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

# Definición de la clase Tienda
# Esta clase administra el inventario de productos
class Tienda:

    # Constructor de la clase Tienda
    def __init__(self):
        # Lista que almacena los productos disponibles en la tienda
        self.productos = []

    # Método que agrega un producto al inventario
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método que muestra todos los productos disponibles
    def mostrar_productos(self):
        print("\nProductos disponibles en la tienda:")
        # Se enumeran los productos para mostrarlos con un número
        for i, producto in enumerate(self.productos, start=1):
            print(f"{i}. ", end="")
            producto.mostrar_info()

    # Método que retorna un producto según su índice
    def obtener_producto(self, indice):
        # Verifica que el índice sea válido
        if 0 <= indice < len(self.productos):
            return self.productos[indice]
        else:
            print("Producto no válido.")
            return None
