# --------------------------------------------------------------
# Tarea Práctica: Programación Tradicional vs Programación Orientada a Objetos
# Tema: Cálculo del promedio semanal de temperaturas
#
# En este código se aplica PROGRAMACIÓN TRADICIONAL:
#  - Uso de funciones independientes
#  - Flujo lineal de ejecución
# --------------------------------------------------------------

# Función para ingresar las temperaturas de los 7 días de la semana
def ingresar_temperaturas():
    """
    Solicita al usuario ingresar la temperatura de cada día de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese las temperaturas de la semana:")

    for dia in dias:
        temp = float(input(f"Temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    """
    Recibe una lista de temperaturas y retorna el promedio.
    """
    return sum(temperaturas) / len(temperaturas)


# Programa principal utilizando programación tradicional
def main():
    datos = ingresar_temperaturas()         # Entrada de datos
    promedio = calcular_promedio(datos)     # Proceso

    print(f"\nEl promedio semanal es: {promedio:.2f}°C")   # Salida


# Ejecución del programa
main()

