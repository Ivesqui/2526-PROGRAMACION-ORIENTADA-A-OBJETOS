class Vehiculo:
    """
    Modelo que representa un vehículo en el sistema de garaje.
    """

    def __init__(self, placa: str, marca: str, propietario: str):
        """
        Inicializa un nuevo vehículo.

        Args:
            placa: Placa o matrícula del vehículo
            marca: Marca del vehículo
            propietario: Nombre del propietario
        """
        self._placa = placa.upper()
        self._marca = marca
        self._propietario = propietario

    @property
    def placa(self) -> str:
        """Obtiene la placa del vehículo."""
        return self._placa

    @property
    def marca(self) -> str:
        """Obtiene la marca del vehículo."""
        return self._marca

    @property
    def propietario(self) -> str:
        """Obtiene el propietario del vehículo."""
        return self._propietario

    def __str__(self) -> str:
        """Representación en string del vehículo."""
        return f"Vehículo(placa={self.placa}, marca={self.marca}, propietario={self.propietario})"

    def __repr__(self) -> str:
        """Representación técnica del vehículo."""
        return self.__str__()