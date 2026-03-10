# Universidad Estatal Amazónica

# 🚗 Sistema Básico de Gestión de Garaje

# Proyecto desarrollado para la Semana 13 aplicando interfaces gráficas de usuario (GUI) con Tkinter y una arquitectura modular por capas.

# 🎯 Objetivo del Proyecto

Desarrollar una aplicación de escritorio que permita registrar y visualizar vehículos dentro de un garaje mediante una interfaz gráfica.

El sistema permite:

- Registrar vehículos
- Visualizar vehículos registrados en una tabla
- Eliminar vehículos
- Limpiar campos del formulario
- Exportar la lista de vehículos a un archivo .txt

El proyecto implementa una separación clara entre:

- Modelos (entidades)
- Servicios (lógica del negocio)
- Interfaz gráfica
- Punto de entrada del sistema

# 🏗️ Arquitectura del Proyecto

El sistema está organizado bajo una arquitectura modular por capas.

```
garaje_app/
│
├── main.py
│
├── modelos/
│   └── vehiculo.py
│
├── servicios/
│   └── garaje_servicio.py
│
└── ui/
    └── app_tkinter.py
```

### 🔹 modelos/

Contiene las clases que representan las entidades del sistema.

vehiculo.py

Representa un vehículo dentro del garaje.

Atributos principales:

- placa
- marca
- propietario

Esta capa solo contiene estructuras de datos, sin lógica del negocio.

### 🔹 servicios/

Contiene la clase GarajeServicio, responsable de la lógica del sistema.

Gestiona:

- Registro de vehículos
- Búsqueda de vehículos por placa
- Eliminación de vehículos
- Conteo de vehículos registrados

También valida que no existan placas duplicadas dentro del sistema.

### 🔹 ui/

Contiene la interfaz gráfica desarrollada con Tkinter.

Archivo principal:

app_tkinter.py

La interfaz incluye:

- Ventana principal
- Formulario de ingreso de datos
- Botones de acción
- Tabla de vehículos registrados

La UI solo maneja interacción con el usuario, sin lógica del negocio.

### 🔹 main.py

Es el punto de entrada de la aplicación.

Se encarga de:

- Inicializar Tkinter
- Crear la ventana principal
- Ejecutar la aplicación


# 🚗 Validaciones Implementadas

El sistema incluye validaciones para mejorar la integridad de los datos.

✔ Validación de campos obligatorios

No se permite registrar vehículos con campos vacíos.

✔ Validación de formato de placa

Formato permitido:

PBC-4827

# 📄 Exportación de Datos

El sistema permite exportar los vehículos registrados a un archivo:

vehiculos.txt

Ejemplo de salida:

```
LISTA DE VEHÍCULOS
---------------------------
Placa: PBC-4827 | Marca: Toyota | Propietario: Carlos Mendoza
Placa: ZXA-3048 | Marca: Hyundai | Propietario: Luis Ramírez
```

## 🚀 Cómo Ejecutar el Proyecto
1️⃣ Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
2️⃣ Entrar al proyecto
cd garaje_app
3️⃣ Ejecutar la aplicación
python main.py

Se abrirá la ventana de la aplicación.

👨‍💻 Autor

Christian Iván Estupiñán Quintero
2do A 
Semana 13 – Interfaces Gráficas con Tkinter
Programación Orientada a Objetos