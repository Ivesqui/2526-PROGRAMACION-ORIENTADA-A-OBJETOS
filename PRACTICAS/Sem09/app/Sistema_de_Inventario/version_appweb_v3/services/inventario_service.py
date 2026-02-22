from datetime import datetime
from core.entities.producto import Producto


class InventarioService:

    def __init__(self, repository):
        self.repository = repository

    def crear_producto(self, producto: Producto):
        if not producto.sku or not producto.nombre_producto:
            raise ValueError("SKU y nombre son obligatorios")

        if self.repository.obtener_por_sku(producto.sku):
            raise ValueError("El SKU ya existe")

        self.repository.guardar(producto)

    def listar_productos(self):
        return self.repository.obtener_todos()

    def buscar_por_sku(self, sku: str):
        return self.repository.obtener_por_sku(sku)

    def actualizar_producto(self, producto: Producto):
        producto.fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.repository.actualizar(producto)

    def eliminar_producto(self, sku: str):
        self.repository.eliminar_logico(sku)