# Sistema de Préstamo de Biblioteca (POO)

## 📌 Descripción del Proyecto
Este proyecto implementa un **sistema básico de préstamo de libros** utilizando
**Programación Orientada a Objetos (POO)** en Python y ejecutándose en **consola**.

El sistema modela una situación real de una biblioteca, permitiendo gestionar libros,
usuarios y préstamos mediante una arquitectura modular y organizada.

---

## 🎯 Objetivo
Aplicar los principios fundamentales de la Programación Orientada a Objetos mediante:
- Uso de clases y objetos
- Encapsulación de responsabilidades
- Interacción entre entidades del mundo real
- Organización del código en módulos independientes

---
## 🗂️ Estructura del Proyecto

```bash
SistemaBiblioteca/
├── main.py          # Programa principal
├── libro.py         # Clase Libro
├── usuario.py       # Clase Usuario
├── biblioteca.py    # Clase Biblioteca
└── README.md        # Documentación del sistema
```

## ⚙️ Funcionalidades del Sistema

### 1️⃣ Mostrar libros disponibles
- Permite visualizar todos los libros registrados en la biblioteca.
- Muestra título, autor y estado del libro (Disponible o Prestado).

### 2️⃣ Prestar un libro
- El usuario puede seleccionar un libro desde el listado.
- El sistema verifica si el libro está disponible.
- Si está disponible:
  - El libro cambia su estado a **prestado**.
  - Se agrega el libro a la lista de libros prestados del usuario.
- Si no está disponible, se muestra un mensaje de error.

### 3️⃣ Ver libros prestados por el usuario
- Muestra todos los libros que el usuario tiene actualmente en préstamo.
- Si no tiene libros prestados, el sistema lo indica.

### 4️⃣ Menú interactivo en consola
- El sistema presenta un menú con opciones claras.
- Permite navegar entre las funcionalidades de forma sencilla.
- Incluye validación básica de entradas.

### 5️⃣ Salir del sistema
- Finaliza la ejecución del programa de forma controlada.

---

## 🧩 Descripción de Clases

### 📘 Clase `Libro`
Representa un libro de la biblioteca.

**Atributos:**
- `titulo`
- `autor`
- `disponible`

**Métodos principales:**
- `mostrar_info()`
- `prestar()`

---

### 👤 Clase `Usuario`
Representa a un usuario de la biblioteca.

**Atributos:**
- `nombre`
- `libros_prestados`

**Métodos principales:**
- `agregar_libro(libro)`
- `mostrar_libros()`

---

### 🏛️ Clase `Biblioteca`
Gestiona el inventario de libros.

**Atributos:**
- `libros`

**Métodos principales:**
- `agregar_libro(libro)`
- `mostrar_libros()`
- `obtener_libro(indice)`

---

## 🧠 Principios de POO Aplicados

- **Encapsulación:** cada clase maneja su propia información.
- **Abstracción:** se modelan entidades reales como libros y usuarios.
- **Interacción entre objetos:** el usuario interactúa con la biblioteca y los libros.
- **Modularización:** el sistema se divide en archivos independientes.

---

## ▶️ Ejecución del Programa

Para ejecutar el sistema:

```bash
python main.py


