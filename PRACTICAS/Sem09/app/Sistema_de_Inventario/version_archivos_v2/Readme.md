# Universidad Estatal Amazónica  
- **Carrera:** Tecnologías de la Información  
- **Asignatura:** Programación Orientada a Objetos  
- **Curso:** 2do A  
- **Estudiante:** Christian Iván Estupiñán Quintero  

---

# Sistema de Gestión de Inventarios – Versión con Archivos

Este proyecto corresponde a la versión mejorada del Sistema de Gestión de Inventarios, desarrollada como parte de la asignatura **Programación Orientada a Objetos**.

En esta versión se reemplaza el uso de base de datos por **persistencia mediante archivos de texto**, implementando además un manejo robusto de excepciones durante la lectura y escritura de datos.

---

## 🎯 Objetivo de la Mejora

El objetivo principal de esta versión es:

- Implementar almacenamiento de datos en un archivo de texto (`inventario.txt`).
- Reconstruir automáticamente el inventario al iniciar el programa.
- Manejar correctamente excepciones relacionadas con archivos.
- Mantener una arquitectura modular aplicando principios de POO.

---

## 📌 Descripción del Sistema

El Sistema de Gestión de Inventarios es una aplicación de consola que permite:

- Registrar productos.
- Desactivar productos (sin eliminarlos físicamente).
- Actualizar stock y precios.
- Buscar productos por nombre o SKU.
- Listar todos los productos.
- Persistir la información en un archivo de texto.

---

## 💾 Persistencia de Datos

La información se almacena en un archivo llamado:

```
inventario.txt
```
Cada línea del archivo representa un producto con el siguiente formato:
```
sku|nombre|categoria|unidad|precio_compra|precio_venta|stock_actual|stock_minimo

Ejemplo:

ALM-001|Arroz|Alimentos|kg|1.20|1.50|50|10|True
```

Cuando el programa inicia:

1. Se intenta leer el archivo `inventario.txt`.
2. Se reconstruyen los objetos `Producto`.
3. Si el archivo no existe, se crea automáticamente.

---

## ⚠️ Manejo de Excepciones

El sistema implementa manejo de excepciones para:

- `FileNotFoundError` → Si el archivo no existe, se crea automáticamente.
- `PermissionError` → Si no hay permisos para leer o escribir.
- `ValueError` → Validación de datos ingresados por el usuario.
- Excepciones generales durante lectura o escritura.

Esto garantiza que el sistema no se detenga inesperadamente ante errores de archivo.

---

## 🧱 Arquitectura del Proyecto

El proyecto mantiene una estructura modular organizada en capas:

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


### 📦 modelos/
Contiene la clase `Producto`, responsable de:
- Validaciones de negocio.
- Encapsulamiento de atributos.
- Representación de un producto del inventario.

### 🛠 servicios/
Contiene la clase `Inventario`, responsable de:
- Lógica de negocio.
- Lectura y escritura del archivo.
- Gestión del inventario en memoria.

### 🖥 interfaz/
Contiene el menú de consola que permite la interacción con el usuario.

---

## ⚙️ Funcionalidades del Sistema

### 1️⃣ Registrar Producto
- Valida datos.
- Verifica que el SKU no exista.
- Guarda automáticamente en el archivo.

### 2️⃣ Dar de Baja Producto
- Cambia el estado del producto a inactivo.
- Actualiza el archivo.

### 3️⃣ Actualizar Stock o Precios
- Permite modificar stock, precio de compra y precio de venta.
- Guarda cambios automáticamente.

### 4️⃣ Buscar Producto
- Búsqueda parcial por SKU o nombre.

### 5️⃣ Listar Inventario
- Muestra todos los productos.
- Indica si están activos o inactivos.

---

## 🧠 Principios de POO Aplicados

- Encapsulamiento (atributos privados en la clase `Producto`)
- Separación de responsabilidades
- Modularización
- Reutilización de código
- Manejo controlado de errores

---

## ▶️ Cómo Ejecutar el Proyecto

1. Asegurarse de tener instalado Python 3.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

python main.py


El archivo `inventario.txt` se creará automáticamente si no existe.

---

## 📚 Conclusión

Esta versión del Sistema de Gestión de Inventarios demuestra:

- Implementación de persistencia en archivos de texto.
- Manejo robusto de excepciones.
- Aplicación correcta de Programación Orientada a Objetos.
- Separación clara entre modelo, lógica de negocio e interfaz.

El sistema simula el funcionamiento básico de un inventario real utilizando únicamente archivos de texto, cumpliendo con los requisitos académicos establecidos.
