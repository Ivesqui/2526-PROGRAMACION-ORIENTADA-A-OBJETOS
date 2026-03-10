from typing import List
from modelos.vehiculo import Vehiculo


class GarajeServicio:
    """
    Servicio que maneja la lógica de negocio del garaje.
    Gestiona el registro y consulta de vehículos.
    """

    def __init__(self):
        """Inicializa el servicio con una lista vacía de vehículos."""
        self._vehiculos: List[Vehiculo] = []

    def agregar_vehiculo(self, vehiculo: Vehiculo) -> bool:
        """
        Agrega un vehículo al garaje.

        Args:
            vehiculo: Objeto Vehiculo a agregar

        Returns:
            True si se agregó exitosamente, False si la placa ya existe
        """
        # Verificar que la placa no exista
        if self.buscar_por_placa(vehiculo.placa):
            return False

        self._vehiculos.append(vehiculo)
        return True

    def buscar_por_placa(self, placa: str) -> Vehiculo | None:
        """
        Busca un vehículo por su placa.

        Args:
            placa: Placa del vehículo a buscar

        Returns:
            Objeto Vehiculo si se encuentra, None si no existe
        """
        placa_upper = placa.upper()
        for vehiculo in self._vehiculos:
            if vehiculo.placa.upper() == placa_upper:
                return vehiculo
        return None

    def obtener_todos(self) -> List[Vehiculo]:
        """
        Obtiene todos los vehículos registrados.

        Returns:
            Lista de todos los vehículos
        """
        return self._vehiculos.copy()

    def contar_vehiculos(self) -> int:
        """
        Cuenta el total de vehículos registrados.

        Returns:
            Número total de vehículos
        """
        return len(self._vehiculos)

    def eliminar_vehiculo(self, placa: str) -> bool:
        """
        Elimina un vehículo del garaje por su placa.
        """
        placa_upper = placa.upper()

        # Recorremos la lista interna de vehículos registrados
        # y comparamos cada placa con la placa que queremos eliminar.
        # Usamos upper() para evitar problemas de mayúsculas/minúsculas.
        for vehiculo in self._vehiculos:
            if vehiculo.placa.upper() == placa_upper:
                # Si encontramos coincidencia, eliminamos ese vehículo de la lista
                self._vehiculos.remove(vehiculo)
                return True

        # Si terminamos el recorrido y no encontramos la placa,
        # significa que el vehículo no estaba registrado
        return False