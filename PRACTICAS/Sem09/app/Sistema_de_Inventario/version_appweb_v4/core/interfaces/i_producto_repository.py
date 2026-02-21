from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.producto import Producto

class IProductoRepository(ABC):
    """
    Interfaz para el Repositorio de Productos.
    Define qué debe hacer cualquier persistencia (SQLite, Postgres, etc).
    """

    @abstractmethod
    def guardar(self, producto: Producto) -> bool:
        pass

    @abstractmethod
    def obtener_por_sku(self, sku: str) -> Optional[Producto]:
        pass

    @abstractmethod
    def listar_todos(self) -> List[Producto]:
        pass

    @abstractmethod
    def actualizar_stock(self, sku: str, nueva_cantidad: int) -> bool:
        pass