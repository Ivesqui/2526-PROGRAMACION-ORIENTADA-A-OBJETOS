from modelos.servicio import Servicio

class ServicioLuz(Servicio):
    """
    Servicio Eléctrico
    Tarifa nacional fija
    """

    TARIFA_KWH = 0.0797
    CARGO_FIJO = 1.41
    SUBSIDIO = 4.96

    def __init__(self, codigo, consumo, mes, fecha_pago):
        super().__init__(codigo, "Luz Eléctrica", consumo, mes, fecha_pago)

        self.agregar_tasa("Alumbrado Público", 0.00)

    def calcular_costo(self):
        costo = (
            self.get_consumo() * self.TARIFA_KWH
            + self.CARGO_FIJO
            - self.SUBSIDIO
            + sum(self.tasas.values())
        )
        return round(costo, 2)
