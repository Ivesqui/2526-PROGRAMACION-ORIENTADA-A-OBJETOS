# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

# Definición de la clase Producto
# Esta clase representa un producto que se vende en la tienda
class Producto:

    # Constructor de la clase
    # Se ejecuta cuando se crea un nuevo objeto Producto
    def __init__(self, nombre, precio, stock):
        # Atributo que almacena el nombre del producto
        self.nombre = nombre
        # Atributo que almacena el precio del producto
        self.precio = precio
        # Atributo que almacena la cantidad disponible en stock
        self.stock = stock

    # Método que muestra la información del producto
    def mostrar_info(self):
        print(f"{self.nombre} | Precio: ${self.precio} | Stock: {self.stock}")

    # Método que reduce el stock del producto
    # Se utiliza cuando un cliente realiza una compra
    def reducir_stock(self, cantidad):
        # Verifica si hay suficiente stock disponible
        if cantidad <= self.stock:
            # Reduce el stock
            self.stock -= cantidad
            return True
        else:
            # Mensaje en caso de no haber stock suficiente
            print("No hay suficiente stock disponible.")
            return False
