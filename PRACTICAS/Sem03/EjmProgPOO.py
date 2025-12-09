# --------------------------------------------------------------
# Tarea Práctica: Programación Orientada a Objetos (POO)
# Tema: Cálculo del promedio semanal del clima
#
# En este código se aplican los principios de POO:
#  - Clases (ClimaDia y ClimaSemana)
#  - Encapsulamiento (atributo privado __temperatura)
#  - Herencia (ClimaSemanaExtendida)
#  - Polimorfismo (sobrescritura del método promedio_semanal)
# --------------------------------------------------------------


# Clase que representa un día con su temperatura
class ClimaDia:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.__temperatura = temperatura  # Atributo encapsulado

    # Getter de la temperatura
    def obtener_temperatura(self):
        """
        Retorna la temperatura almacenada.
        """
        return self.__temperatura

    # Setter de la temperatura
    def asignar_temperatura(self, nueva_temp):
        """
        Permite modificar la temperatura del día.
        """
        self.__temperatura = nueva_temp


# Clase que representa una semana completa
class ClimaSemana:
    def __init__(self):
        self.dias = []   # Lista de objetos ClimaDia

    def ingresar_datos(self):
        """
        Solicita las temperaturas de los 7 días y crea objetos ClimaDia.
        """
        nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves",
                        "Viernes", "Sábado", "Domingo"]

        for dia in nombres_dias:
            temp = float(input(f"Temperatura del {dia}: "))
            self.dias.append(ClimaDia(dia, temp))

    def promedio_semanal(self):
        """
        Calcula el promedio tomando la temperatura de cada objeto ClimaDia.
        """
        total = sum(d.obtener_temperatura() for d in self.dias)
        return total / len(self.dias)


# Clase extendida para demostrar herencia y polimorfismo
class ClimaSemanaExtendida(ClimaSemana):

    def promedio_semanal(self):
        """
        Redefinimos el método para añadir un mensaje extra.
        (Ejemplo de polimorfismo)
        """
        print("Cálculo realizado con ClimaSemanaExtendida.")
        return super().promedio_semanal()


# Programa principal con POO
def main():
    clima = ClimaSemanaExtendida()  # Uso de herencia
    clima.ingresar_datos()
    promedio = clima.promedio_semanal()

    print(f"\nEl promedio semanal es: {promedio:.2f}°C")


# Ejecución del programa
main()

