# 📚 Sistema de Gestión de Biblioteca Digital

Proyecto desarrollado para la **Semana 12** aplicando Programación Orientada a Objetos (POO) y una arquitectura estructurada por capas.

---

## 🎯 Objetivo del Proyecto

Desarrollar un sistema de gestión de biblioteca digital que permita administrar:

- Libros
- Usuarios
- Préstamos y devoluciones
- Búsquedas avanzadas en el catálogo

El proyecto implementa una separación clara entre:

- **Modelos (entidades)**
- **Servicios (lógica del negocio)**
- **Interfaz (menú en consola)**
- **Punto de entrada (main)**

---

## 🏗️ Arquitectura del Proyecto

El sistema está organizado bajo una arquitectura por capas:

```
biblioteca_app/
│
├── modelos/
│ ├── libro.py
│ └── usuario.py
│
├── servicios/
│ └── biblioteca_servicio.py
│
├── interfaz/
│ └── menu.py
│
└── main.py
```

### 🔹 modelos/
Contiene únicamente las clases que representan entidades del sistema:
- `Libro`
- `Usuario`

No contiene lógica de negocio.

---

### 🔹 servicios/
Contiene la clase `BibliotecaServicio`, que gestiona:
- Catálogo de libros
- Registro de usuarios
- Préstamos y devoluciones
- Búsquedas

Aquí se concentra toda la lógica del sistema.

---

### 🔹 interfaz/
Contiene la clase `Menu`, encargada únicamente de la interacción con el usuario por consola.

No contiene lógica de negocio.

---

### 🔹 main.py
Es el punto de entrada del sistema.  
Inicializa los componentes y ejecuta el programa.

---

## 🧠 Conceptos Aplicados

### ✔ Programación Orientada a Objetos
- Encapsulamiento
- Métodos bien definidos
- Separación de responsabilidades

### ✔ Uso obligatorio de colecciones

| Requisito | Implementación |
|-----------|---------------|
| Tupla | (Título, Autor) en la clase `Libro` |
| Lista | Libros prestados en la clase `Usuario` |
| Diccionario | Catálogo de libros (clave: ISBN) |
| Set | Control de IDs únicos de usuarios |

---

## 📘 Funcionalidades Implementadas

### 📚 Gestión de Libros
- Añadir libro (incluye año de publicación)
- Eliminar libro (solo si no está prestado)
- Estado del libro:
  - Disponible (estado inicial)
  - Prestado

---

### 👤 Gestión de Usuarios
- Registrar usuario
- Dar de baja usuario

---

### 🔁 Préstamos
- Prestar libro
- Devolver libro
- Validación de disponibilidad
- Actualización automática del estado

---

### 🔍 Búsquedas Avanzadas
Búsqueda parcial (no requiere coincidencia exacta):

- Por título (ej: "moby" encuentra "Moby Dick")
- Por autor (ej: "melville")
- Por categoría
- Por año de publicación

---

### 📋 Listado
- Listar libros prestados por un usuario

---

## 🚀 Cómo Ejecutar el Proyecto

1. Clonar el repositorio:
```
git clone <URL_DEL_REPOSITORIO>
```
2. Ingresar al directorio del proyecto:
```
cd biblioteca_app
```
3. Ejecutar el sistema:
```
python main.py
```

---

## 🔐 Decisiones de Diseño

- El ISBN se utiliza como identificador único del libro.
- Los libros no se eliminan del catálogo cuando se prestan.
- El estado del libro se gestiona dentro del modelo `Libro`.
- La interfaz está completamente desacoplada del servicio.

Esto garantiza una arquitectura clara y mantenible.

---

## 🏆 Resultado

El sistema cumple con:

✔ Separación por capas  
✔ Uso correcto de estructuras de datos  
✔ Aplicación de POO  
✔ Menú interactivo funcional  
✔ Gestión completa del flujo biblioteca  

---

## 👨‍💻 Autor

Christian Iván Estupiñán Quintero  
Semana 12 – Arquitectura por Capas  
Programación Orientada a Objetos

---````