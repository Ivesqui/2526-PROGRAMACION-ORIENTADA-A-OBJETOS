from modelos.servicio_agua import ServicioAgua
from modelos.servicio_luz import ServicioLuz
from modelos.servicio_internet import ServicioInternet
from servicios.gestor_servicios import GestorServicios
from servicios.exportador_excel import exportar_a_excel

gestor = GestorServicios()

while True:
    print("\n--- CONTROL DE SERVICIOS BÁSICOS ---")
    print("1. Registrar consumo de Agua")
    print("2. Registrar consumo de Luz")
    print("3. Registrar Internet")
    print("4. Exportar a Excel")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = input("Código del servicio: ")
        mes = input("Mes facturado: ")
        fecha = input("Fecha máxima de pago: ")
        consumo = float(input("Consumo de agua (m3): "))

        agua = ServicioAgua(codigo, consumo, mes, fecha)
        gestor.agregar_servicio(agua)

    elif opcion == "2":
        codigo = input("Código del servicio: ")
        mes = input("Mes facturado: ")
        fecha = input("Fecha máxima de pago: ")
        consumo = float(input("Consumo eléctrico (kWh): "))

        luz = ServicioLuz(codigo, consumo, mes, fecha)
        gestor.agregar_servicio(luz)

    elif opcion == "3":
        codigo = input("Código del servicio: ")
        mes = input("Mes facturado: ")
        fecha = input("Fecha máxima de pago: ")

        internet = ServicioInternet(codigo, mes, fecha)
        gestor.agregar_servicio(internet)

    elif opcion == "4":
        exportar_a_excel(gestor.obtener_resumen())
        print("Excel generado correctamente.")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break
