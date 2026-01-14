class GestorServicios:
    """
    Clase encargada de administrar múltiples servicios
    """

    def __init__(self):
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def obtener_resumen(self):
        return [s.obtener_detalle() for s in self.servicios]
