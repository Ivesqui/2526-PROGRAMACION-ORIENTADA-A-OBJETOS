# Tarea Práctica: Comparación de Programación Tradicional
# y POO en Python
#
# Objetivo: Desarrollar habilidades prácticas
# en la Programación Tradicional y la Programación Orientada a Objetos
# (POO) mediante la implementación de un programa en Python para
# determinar el promedio semanal del clima.

# Función para ingresar las temperaturas del día durante toda la semana
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de la semana:")

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        temp = float(input(f"Temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


# Programa principal
def main():
    datos = ingresar_temperaturas()
    promedio = calcular_promedio(datos)
    print(f"\nEl promedio semanal es: {promedio:.2f}°C")


main()
