# ==========================================
# Nombre: Christian Iván Estupiñán Quintero
# Asignatura: Programación Orientada a Objetos
# Curso: 2do Ingeniería en Tecnologías de la Información "A"
# PAO: 2025-2026
# ==========================================

# Importación de las clases necesarias
from Producto import Producto
from Cliente import Cliente
from Tienda import Tienda

# Función que muestra el menú principal del sistema
def mostrar_menu():
    print("\n--- MENÚ DE LA TIENDA ---")
    print("1. Ver productos")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito")
    print("4. Salir")

# Función principal del programa
def main():
    # Creación de la tienda
    tienda = Tienda()

    # Creación del cliente
    cliente = Cliente("Juan Pérez")

    # Agregar productos al inventario de la tienda
    tienda.agregar_producto(Producto("Laptop", 800, 5))
    tienda.agregar_producto(Producto("Mouse", 20, 10))
    tienda.agregar_producto(Producto("Teclado", 35, 7))

    # Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # Opción para mostrar productos
        if opcion == "1":
            tienda.mostrar_productos()

        # Opción para agregar productos al carrito
        elif opcion == "2":
            tienda.mostrar_productos()

            try:
                # Solicita el producto y la cantidad
                indice = int(input("Seleccione el número del producto: ")) - 1
                cantidad = int(input("Ingrese la cantidad: "))

                # Obtiene el producto seleccionado
                producto = tienda.obtener_producto(indice)

                # Verifica stock y agrega al carrito
                if producto and producto.reducir_stock(cantidad):
                    cliente.agregar_al_carrito(producto, cantidad)
                    print("Producto agregado al carrito.")

            except ValueError:
                # Manejo de error si el usuario ingresa valores no numéricos
                print("Entrada inválida. Debe ingresar números.")

        # Opción para ver el carrito
        elif opcion == "3":
            cliente.mostrar_carrito()

        # Opción para salir del sistema
        elif opcion == "4":
            print("Gracias por usar el sistema.")
            break

        # Opción inválida
        else:
            print("Opción no válida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
