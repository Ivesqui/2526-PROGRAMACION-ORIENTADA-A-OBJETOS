# ================================
# Clase base Servicio
# ================================
# Aplica ABSTRACCIÓN, HERENCIA y POLIMORFISMO

class Servicio:
    def __init__(self, codigo, nombre, consumo, mes, fecha_pago):
        self.codigo = codigo
        self.nombre = nombre
        self.__consumo = consumo   # Encapsulación
        self.mes = mes
        self.fecha_pago = fecha_pago

        # Diccionario de tasas estándar
        self.tasas = {}

    # Getter del consumo
    def get_consumo(self):
        return self.__consumo

    # Permite agregar tasas sin modificar clases
    def agregar_tasa(self, nombre, valor):
        self.tasas[nombre] = valor

    # Método abstracto (polimorfismo)
    def calcular_costo(self):
        raise NotImplementedError("Debe implementar calcular_costo")

    # ✅ MÉTODO QUE FALTABA
    def obtener_detalle(self):
        """
        Retorna la información común del servicio.
        Las clases hijas solo calculan el total.
        """
        return {
            "Código": self.codigo,
            "Servicio": self.nombre,
            "Mes": self.mes,
            "Fecha Máx. Pago": self.fecha_pago,
            "Consumo": self.get_consumo(),
            "Total a Pagar": self.calcular_costo()
        }
