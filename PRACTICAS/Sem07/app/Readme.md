# Sistema de Registro de Usuarios en Python sencillo

## Universidad Estatal Amazónica
Carrera: Tecnologías de la Información  
Asignatura: Programación Orientada a Objetos  
Curso: 2do A  
Estudiante: Christian Iván Estupiñán Quintero  

---

## 📌 Descripción
Sistema desarrollado en **Python** que permite registrar y gestionar usuarios
mediante el uso de **constructores (__init__) y destructores (__del__)**.

El programa aplica los principios básicos de la **Programación Orientada a Objetos (POO)**,
utilizando una arquitectura separada por capas:

- Modelos  
- Servicios  
- Programa principal  

Esta aplicación representa una **versión simplificada**, creada con fines académicos,
cuyo objetivo principal es evidenciar el ciclo de vida de los objetos en Python.

En futuras versiones se podrá ampliar para incluir persistencia avanzada,
interfaces gráficas y gestión completa de usuarios.

---

## ⚙️ Características principales
- Creación de usuarios mediante clases
- Inicialización automática de atributos con el constructor
- Apertura y uso de un archivo como recurso del sistema
- Liberación de recursos usando el destructor
- Registro automático de eventos
- Arquitectura modular y organizada
- Código claro y documentado

---

## 🧪 Tipos de Datos Utilizados
- `string`: nombre, correo electrónico
- `list`: almacenamiento temporal de usuarios
- `bool`: validaciones internas
- `file`: manejo de archivo de texto como recurso
- `object`: instancias de clases

---

## ▶️ Ejecución

1. Ejecutar el programa desde el archivo principal:


2. Al ejecutarse, el sistema:

- creará automáticamente la carpeta `data/`
- generará el archivo `usuarios.txt`
- registrará la creación y eliminación de usuarios

---

## 🗂️ Estructura del Proyecto

---
```
sistema_registro_simple/
├── main.py
├── data/
│ └── usuarios.txt
├── modelos/
│ └── usuario.py
├── servicios/
│ └── usuario_servicio.py
└── README.md
```
