# Explicación del Sistema de Tienda (POO)
## Datos del estudiante

#### Nombre: Christian Iván Estupiñán Quintero
#### Asignatura: Programación Orientada a Objetos
#### Curso: 2do Ingeniería en Tecnologías de la Información "A"
#### PAO: 2025-2026

## Descripción General
Este proyecto modela una tienda básica utilizando los principios de la Programación
Orientada a Objetos (POO). El sistema representa entidades del mundo real como productos,
clientes y una tienda, permitiendo gestionar un inventario y simular el proceso de compra
mediante un menú interactivo.

El programa está organizado en módulos, lo que facilita la lectura, el mantenimiento
y la reutilización del código.

---

## Archivo `producto.py`

### Clase Producto
Representa un producto disponible en la tienda.

**Atributos:**
- `nombre`: nombre del producto.
- `precio`: precio unitario del producto.
- `stock`: cantidad disponible en inventario.

**Métodos:**
- `mostrar_info()`: muestra en pantalla la información del producto.
- `reducir_stock(cantidad)`: reduce el stock del producto cuando se realiza una compra,
  verificando que exista suficiente cantidad disponible.

---

## Archivo `cliente.py`

### Clase Cliente
Representa a un cliente que realiza compras en la tienda.

**Atributos:**
- `nombre`: nombre del cliente.
- `carrito`: lista que almacena los productos seleccionados junto con sus cantidades.

**Métodos:**
- `agregar_al_carrito(producto, cantidad)`: agrega un producto y su cantidad al carrito
  del cliente.
- `mostrar_carrito()`: muestra los productos que el cliente ha agregado al carrito.

---

## Archivo `tienda.py`

### Clase Tienda
Representa la tienda y se encarga de gestionar el inventario de productos.

**Atributos:**
- `productos`: lista que contiene los productos disponibles en la tienda.

**Métodos:**
- `agregar_producto(producto)`: agrega un producto al inventario de la tienda.
- `mostrar_productos()`: muestra todos los productos disponibles con su información.
- `obtener_producto(indice)`: devuelve un producto según el índice seleccionado por
  el usuario, validando que sea correcto.

---

## Archivo `main.py`

### Función principal
Este archivo controla la ejecución del sistema y la interacción con el usuario.

**Funciones principales:**
- Crea la tienda y el cliente.
- Agrega productos al inventario de la tienda.
- Presenta un menú interactivo para:
  - Ver productos disponibles.
  - Agregar productos al carrito.
  - Ver el carrito de compras.
  - Salir del sistema.

Este archivo integra todos los módulos y permite observar la interacción entre las
clases `Producto`, `Cliente` y `Tienda`.

---

## Conclusión
El proyecto demuestra los principios fundamentales de la Programación Orientada a Objetos:

- **Encapsulación:** cada clase tiene responsabilidades bien definidas.
- **Uso de clases y objetos:** se modelan entidades reales mediante clases.
- **Interacción entre objetos:** el cliente compra productos a través de la tienda.
- **Organización modular:** el sistema se divide en archivos independientes para
  mejorar la claridad y el mantenimiento del código.

Este diseño facilita la ampliación del sistema, por ejemplo, agregando nuevas funciones
como el cálculo del total de la compra o distintos tipos de clientes.
