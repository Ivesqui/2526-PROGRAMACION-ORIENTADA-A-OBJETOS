# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

# Definición de la clase Cliente
# Representa a una persona que compra en la tienda
class Cliente:

    # Constructor de la clase Cliente
    def __init__(self, nombre):
        # Atributo que almacena el nombre del cliente
        self.nombre = nombre
        # Lista que representa el carrito de compras
        # Cada elemento será una tupla (producto, cantidad)
        self.carrito = []

    # Método que agrega un producto al carrito del cliente
    def agregar_al_carrito(self, producto, cantidad):
        # Agrega el producto y la cantidad como una tupla
        self.carrito.append((producto, cantidad))

    # Método que muestra los productos del carrito
    def mostrar_carrito(self):
        print(f"\nCarrito de compras de {self.nombre}:")

        # Verifica si el carrito está vacío
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            # Recorre los productos del carrito
            for producto, cantidad in self.carrito:
                print(f"- {producto.nombre} x {cantidad}")
