# 📌 Promedio Semanal del Clima  
## Comparación entre Programación Tradicional y Programación Orientada a Objetos (POO)

Este repositorio contiene una práctica desarrollada en Python cuyo objetivo es comparar dos enfoques de programación:

- **Programación Tradicional (estructurada)**
- **Programación Orientada a Objetos (POO)**

Ambas soluciones calculan el **promedio semanal de las temperaturas**, ingresadas por el usuario.

## 🧩 Objetivos de la Actividad

1. Aplicar **programación tradicional** mediante funciones.
2. Aplicar **POO en Python** utilizando:
   - Clases
   - Encapsulamiento
   - Herencia
   - Polimorfismo
3. Analizar las diferencias entre ambos enfoques.
4. Organizar y documentar el código para ser publicado en GitHub.

## 📘 Descripción de cada implementación

### 🔷 Programación Tradicional
- Se utilizan **funciones independientes**.
- El flujo del programa es lineal.
- Las funciones principales son:
  - `ingresar_temperaturas()`
  - `calcular_promedio()`
- Adecuado para programas pequeños y simples.

### 🔶 Programación Orientada a Objetos (POO)
- Se crean las clases:
  - `ClimaDia` → Representa cada día con su temperatura (con encapsulamiento).
  - `ClimaSemana` → Contiene la lista de días y calcula el promedio.
  - `ClimaSemanaExtendida` → Ejemplo de herencia y polimorfismo.
- Permite:
  - Organizar mejor la información.
  - Facilitar escalabilidad.
  - Reutilizar código.

## 🆚 Comparativa: Programación Tradicional vs POO

| Aspecto | Programación Tradicional | Programación Orientada a Objetos (POO) |
|---------|---------------------------|-----------------------------------------|
| **Estructura del código** | Basada en funciones y procedimientos sueltos. | Basada en clases y objetos que encapsulan datos y métodos. |
| **Organización** | Secuencial: el flujo del programa domina la lógica. | Modular: cada clase representa un componente independiente. |
| **Reutilización** | Limitada; las funciones pueden volverse repetitivas. | Alta; permite reutilizar clases, herencia y polimorfismo. |
| **Mantenimiento** | Puede volverse complejo al crecer el proyecto. | Facilita mantenimiento gracias a modularidad y abstracción. |
| **Manipulación de datos** | Los datos están separados de las funciones. | Los datos están dentro de los objetos que los gestionan. |
| **Escalabilidad** | Menos adecuada para sistemas grandes. | Ideal para proyectos grandes y colaborativos. |
| **Legibilidad** | Sencilla para programas pequeños. | Más clara y organizada en sistemas complejos. |

