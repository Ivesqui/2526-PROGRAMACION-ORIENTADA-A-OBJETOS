# Universidad Estatal Amazónica  
- **Carrera:** Tecnologías de la Información  
- **Asignatura:** Programación Orientada a Objetos  
- **Curso:** 2do A  
- **Estudiante:** Christian Iván Estupiñán Quintero  

---

# 🏪 Sistema Avanzado de Gestión de Inventario

## 📌 Descripción

Este proyecto consiste en el desarrollo de un **Sistema Avanzado de Gestión de Inventario** para una tienda, implementado en Python aplicando los principios de **Programación Orientada a Objetos (POO)** y el uso eficiente de **colecciones**.

El sistema permite gestionar productos mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y almacena la información de manera persistente en un archivo de texto.

---

# 🎯 Objetivos

- Aplicar correctamente los principios de Programación Orientada a Objetos.
- Utilizar múltiples tipos de colecciones (diccionarios, listas y conjuntos).
- Implementar lectura y escritura de archivos para almacenamiento persistente.
- Construir una interfaz interactiva en consola.
- Organizar el código de forma modular y mantenible.

---

# 🧱 Arquitectura del Proyecto

```
Sistema_de_Inventario/
│
├── modelos/
│ └── producto.py
│
├── servicios/
│ └── inventario.py
│
├── interfaz/
│ └── menu.py
│
├── inventario.txt
├── main.py
└── README.md
```



# 🧩 Clases Principales

## 📦 Clase `Producto`

Representa un producto dentro del inventario.

### Atributos:
- `sku` (ID único)
- `nombre_producto`
- `categoria`
- `unidad`
- `precio_compra`
- `precio_venta`
- `stock_actual`
- `stock_minimo`
- `activo`

### Características:
- Encapsulamiento mediante atributos privados.
- Validaciones de negocio en el constructor.
- Métodos getters y setters controlados.
- Separación de responsabilidades (no maneja archivos).

---

## 🛠 Clase `Inventario`

Es la clase encargada de gestionar los productos y el almacenamiento.

### Colecciones utilizadas

### 1️⃣ Diccionario (estructura principal)

```python
self.__productos = {}

Clave → SKU

Valor → Objeto Producto

Permite búsqueda en tiempo constante O(1).

2️⃣ Conjunto (set)
self.__skus = set()

Garantiza unicidad de los identificadores.

Permite validar rápidamente si un SKU ya existe.

3️⃣ Listas

Se utilizan para:

Retornar resultados de búsqueda.

Listar todos los productos.

Recorrer productos al guardarlos en archivo.

💾 Persistencia en Archivo

El sistema implementa almacenamiento en un archivo de texto plano:

inventario.txt
📌 Formato de almacenamiento

Cada línea del archivo representa un producto y sus atributos separados por el carácter |:

sku|nombre|categoria|unidad|precio_compra|precio_venta|stock_actual|stock_minimo|activo
Ejemplo:
ALM-001|Arroz|Alimentos|kg|1.20|1.50|50|10|True
🔄 Serialización

La serialización se realiza manualmente:

Se recorren los productos almacenados en el diccionario.

Se convierten en una línea de texto delimitada por |.

Se escriben en el archivo.

🔁 Deserialización

Al iniciar el sistema:

Se abre el archivo inventario.txt.

Se lee línea por línea.

Se separan los datos usando split("|").

Se reconstruyen los objetos Producto.

Se repuebla el diccionario y el set.

Esto garantiza persistencia entre ejecuciones.

⚙️ Funcionalidades del Sistema

El sistema incluye un menú interactivo que permite:

1️⃣ Registrar Producto

Valida datos.

Verifica unicidad del SKU.

Guarda automáticamente en archivo.

2️⃣ Eliminar Producto (Eliminación Física)

Elimina completamente el producto del diccionario.

Lo elimina del archivo.

Actualiza el set de SKUs.

3️⃣ Actualizar Producto

Permite modificar:

Stock

Precio de compra

Precio de venta

Guarda automáticamente los cambios.

4️⃣ Buscar Producto

Búsqueda parcial por nombre.

Retorna una lista de coincidencias.

5️⃣ Listar Productos

Muestra todos los productos registrados.

⚠️ Manejo de Excepciones

El sistema implementa manejo de errores para:

FileNotFoundError → Se crea el archivo si no existe.

ValueError → Validación de datos incorrectos.

Excepciones generales durante lectura y escritura.

Esto evita que el programa termine inesperadamente.

🧠 Principios de POO Aplicados

Encapsulamiento

Separación de responsabilidades

Modularización

Persistencia desacoplada del modelo

Validaciones de negocio

Uso eficiente de estructuras de datos

▶️ Cómo Ejecutar

Tener Python 3 instalado.

Ubicarse en la carpeta del proyecto.

Ejecutar:

python main.py

El archivo inventario.txt se creará automáticamente si no existe.