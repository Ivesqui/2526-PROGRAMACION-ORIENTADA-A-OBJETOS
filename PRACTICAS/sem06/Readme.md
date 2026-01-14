# Control de Servicios Básicos en Python (Versión Beta)

## Universidad Estatal Amazónica
Carrera: Tecnologías de la Información  
Asignatura: Programación Orientada a Objetos  
Curso: 2do A  
Estudiante: Christian Iván Estupiñán Quintero  

---

## 📌 Descripción
Sistema desarrollado en **Python** que permite modelar y calcular el valor a pagar de mis **servicios básicos** como:

- 💡 Energía eléctrica  
- 🚰 Agua potable  
- 🌐 Internet  

El proyecto aplica los principios de **Programación Orientada a Objetos (POO)**, utilizando:
- Abstracción  
- Encapsulación  
- Herencia  
- Polimorfismo  

Esta es una **versión beta**, diseñada para ser simple y funcional.  
En futuras versiones se ampliará para trabajar con más servicios y permitir la creación de nuevos servicios.

---

## ⚙️ Características principales
- Tarifas estándar nacionales (no modificables)
- El usuario ingresa únicamente el consumo
- Cálculo automático del total a pagar
- Manejo de tasas fijas (ejemplo: tasa de basura)
- Exportación del resumen a archivo Excel
- Diseño modular y escalable

---

## 🧪 Tipos de Datos Utilizados
- `int`: consumo, códigos de servicio
- `float`: tarifas, tasas, valores monetarios
- `string`: nombre del servicio, mes, fecha de pago
- `list`: almacenamiento de servicios
- `dict`: estructura de datos para exportación a Excel

---

## ▶️ Ejecución
1. Instalar dependencias:

pip install pandas openpyxl

2. Ejecutar el programa desde el archivo principal:

python main.py


Al ejecutarse, el sistema generará el archivo **servicios.xlsx** con el detalle de los servicios registrados.

---
```
## 🗂️ Estructura del Proyecto

control_servicios_basicos/
├── main.py
├── modelos/
│ ├── servicio.py
│ ├── servicio_agua.py
│ ├── servicio_luz.py
│ └── servicio_internet.py
├── servicios/
│ ├── gestor_servicios.py
│ └── exportador_excel.py
└── README.md
```