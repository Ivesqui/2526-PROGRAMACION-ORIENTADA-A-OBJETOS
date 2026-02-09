from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    """
    Muestra en pantalla el menú principal del sistema de inventarios.

    Decisión de diseño:
    - Se separa la visualización del menú de la lógica de ejecución
      para mejorar la legibilidad y facilitar futuras modificaciones.
    """
    print("""
===== SISTEMA DE GESTIÓN DE INVENTARIOS =====
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto
5. Listar inventario
6. Salir
""")


def ejecutar_menu():
    """
    Controla el flujo principal de la aplicación mediante un menú interactivo.

    Lógica implementada:
    - Se crea una instancia de la clase Inventario, que gestiona las operaciones
      sobre los productos.
    - Se utiliza un bucle infinito para mantener el menú activo hasta que
      el usuario decida salir del sistema.
    - Se evalúa la opción ingresada por el usuario y se ejecuta la acción
      correspondiente.

    Decisiones de diseño:
    - El menú opera exclusivamente con el SKU como identificador de negocio,
      evitando el uso del ID técnico interno.
    - Se permite actualizar únicamente los campos necesarios (cantidad y precio),
      haciendo que los parámetros sean opcionales.
    - La interfaz se mantiene simple, basada en consola, para facilitar su uso
      y comprensión.
    """

    # Se crea una instancia del inventario para gestionar los productos
    inventario = Inventario()

    # Bucle principal del sistema
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # AÑADIR PRODUCTO
        if opcion == "1":
            # Se solicitan los datos del producto al usuario
            sku = input("SKU: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            # Se crea un objeto Producto con los datos ingresados
            producto = Producto(sku, nombre, cantidad, precio)

            # Se agrega el producto al inventario
            inventario.agregar_producto(producto)

        # ELIMINAR PRODUCTO POR SKU
        elif opcion == "2":
            # Se solicita el SKU del producto a eliminar
            sku = input("SKU del producto a eliminar: ")
            inventario.eliminar_producto(sku)

        # ACTUALIZAR PRODUCTO POR SKU
        elif opcion == "3":
            # Se solicita el SKU del producto a actualizar
            sku = input("SKU del producto a actualizar: ")

            # Los campos pueden omitirse presionando Enter
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            # Se envían solo los valores ingresados
            inventario.actualizar_producto(
                sku,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        # BUSCAR PRODUCTO (por nombre o SKU)
        elif opcion == "4":
            # Se permite buscar productos usando nombre o SKU
            texto = input("Ingrese nombre o SKU a buscar: ")
            inventario.buscar_producto(texto)

        # LISTAR INVENTARIO
        elif opcion == "5":
            # Se muestran todos los productos registrados
            inventario.listar_productos()

        # SALIR DEL SISTEMA
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        # OPCIÓN INVÁLIDA
        else:
            print("Opción inválida, intente nuevamente")
