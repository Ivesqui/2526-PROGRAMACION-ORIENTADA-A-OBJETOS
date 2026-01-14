from modelos.servicio import Servicio

class ServicioInternet(Servicio):
    """
    Servicio de Internet
    Tarifa fija nacional
    No depende de consumo
    """

    TARIFA_BASE = 24.00
    IVA = 0.12

    def __init__(self, codigo, mes, fecha_pago):
        # Consumo = 0 porque no aplica
        super().__init__(codigo, "Internet", 0, mes, fecha_pago)

    def calcular_costo(self):
        return round(self.TARIFA_BASE * (1 + self.IVA), 2)
