from modelos.servicio import Servicio

class ServicioAgua(Servicio):
    """
    Servicio de Agua Potable
    Tarifas estándar nacionales
    Solo el consumo es modificable
    """

    TARIFA_AGUA = 7.28
    ALCANTARILLADO = 6.95
    CARGO_FIJO = 1.41
    TASA_BASURA = 1.64

    def __init__(self, codigo, consumo, mes, fecha_pago):
        super().__init__(codigo, "Agua Potable", consumo, mes, fecha_pago)

        # Tasa estándar
        self.agregar_tasa("Basura", self.TASA_BASURA)

    def calcular_costo(self):
        costo = (
            self.get_consumo() * self.TARIFA_AGUA
            + self.ALCANTARILLADO
            + self.CARGO_FIJO
            + sum(self.tasas.values())
        )
        return round(costo, 2)
