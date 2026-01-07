"""
Programa de conversión de unidades:
longitud, peso y temperatura.
"""

from modelos.conversion import Conversion
from servicios.servicio_longitud import *
from servicios.servicio_peso import *
from servicios.servicio_temperatura import *


def menu_principal():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Longitud")
    print("2. Peso")
    print("3. Temperatura")
    print("4. Salir")


def menu_longitud():
    print("\n--- Longitud ---")
    print("1. Metros → Kilómetros")
    print("2. Metros → Centímetros")
    print("3. Kilómetros → Metros")
    print("4. Centímetros → Metros")
    print("5. Volver")


def menu_peso():
    print("\n--- Peso ---")
    print("1. Kilogramos → Gramos")
    print("2. Kilogramos → Libras")
    print("3. Gramos → Kilogramos")
    print("4. Libras → Kilogramos")
    print("5. Volver")


def menu_temperatura():
    print("\n--- Temperatura ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Volver")


def ejecutar_programa():
    programa_activo = True  # boolean

    while programa_activo:
        menu_principal()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            while True:
                menu_longitud()
                op = int(input("Seleccione: "))

                if op == 5:
                    break

                valor = float(input("Ingrese el valor: "))
                c = Conversion(valor)

                if op == 1:
                    print(f"Resultado: {m_a_km(c.valor)} km")
                elif op == 2:
                    print(f"Resultado: {m_a_cm(c.valor)} cm")
                elif op == 3:
                    print(f"Resultado: {km_a_m(c.valor)} m")
                elif op == 4:
                    print(f"Resultado: {cm_a_m(c.valor)} m")

        elif opcion == 2:
            while True:
                menu_peso()
                op = int(input("Seleccione: "))

                if op == 5:
                    break

                valor = float(input("Ingrese el valor: "))
                c = Conversion(valor)

                if op == 1:
                    print(f"Resultado: {kg_a_g(c.valor)} g")
                elif op == 2:
                    print(f"Resultado: {kg_a_lb(c.valor)} lb")
                elif op == 3:
                    print(f"Resultado: {g_a_kg(c.valor)} kg")
                elif op == 4:
                    print(f"Resultado: {lb_a_kg(c.valor)} kg")

        elif opcion == 3:
            while True:
                menu_temperatura()
                op = int(input("Seleccione: "))

                if op == 5:
                    break

                valor = float(input("Ingrese el valor: "))
                c = Conversion(valor)

                if op == 1:
                    print(f"Resultado: {c_a_f(c.valor)} °F")
                elif op == 2:
                    print(f"Resultado: {f_a_c(c.valor)} °C")
                elif op == 3:
                    print(f"Resultado: {c_a_k(c.valor)} K")
                elif op == 4:
                    print(f"Resultado: {k_a_c(c.valor)} °C")

        elif opcion == 4:
            print("Saliendo del programa...")
            programa_activo = False

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_programa()
