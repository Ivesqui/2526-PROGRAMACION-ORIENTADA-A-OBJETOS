# Clase que representa un día con su temperatura
class ClimaDia:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.__temperatura = temperatura  # Encapsulamiento

    # Getter de la temperatura
    def obtener_temperatura(self):
        return self.__temperatura

    # Setter de la temperatura
    def asignar_temperatura(self, nueva_temp):
        self.__temperatura = nueva_temp


# Clase que representa la semana completa
class ClimaSemana:
    def __init__(self):
        self.dias = []

    # Mtodo para ingresar las temperaturas de la semana
    def ingresar_datos(self):
        nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        for dia in nombres_dias:
            temp = float(input(f"Temperatura del {dia}: "))
            clima_dia = ClimaDia(dia, temp)
            self.dias.append(clima_dia)

    # Metodos para calcular el promedio
    def promedio_semanal(self):
        total = sum(d.obtener_temperatura() for d in self.dias)
        return total / len(self.dias)


# Ejemplo de Herencia (opcional)
class ClimaSemanaExtendida(ClimaSemana):
    # Polimorfismo: redefinimos el metodo para incluir un mensaje adicional
    def promedio_semanal(self):
        promedio = super().promedio_semanal()
        print("Cálculo realizado con ClimaSemanaExtendida.")
        return promedio


# Programa principal
def main():
    clima = ClimaSemanaExtendida()
    clima.ingresar_datos()
    promedio = clima.promedio_semanal()

    print(f"\nEl promedio semanal es: {promedio:.2f}°C")


main()
