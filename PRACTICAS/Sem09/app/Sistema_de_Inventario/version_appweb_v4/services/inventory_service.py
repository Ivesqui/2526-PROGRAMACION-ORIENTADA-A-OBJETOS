from core.interfaces.i_producto_repository import IProductoRepository
from core.entities.producto import Producto

class InventarioService:
    def __init__(self, repository: IProductoRepository):
        # Inyección de dependencia
        self.repository = repository

    def registrar_producto(self, datos: dict):
        # La lógica de validación ya ocurre dentro de la Entidad Producto
        nuevo_p = Producto(
            sku=datos['sku'],
            nombre_producto=datos['nombre_producto'],
            categoria=datos['categoria'],
            unidad=datos['unidad'],
            precio_compra=datos['precio_compra'],
            precio_venta=datos['precio_venta'],
            stock_actual=datos['stock_actual'],
            stock_minimo=datos['stock_minimo'],
            codigo_barras=datos.get('codigo_barras')
        )
        return self.repository.guardar(nuevo_p)

    def obtener_resumen_dashboard(self):
        productos = self.repository.list_all()
        return {
            "total": len(productos),
            "criticos": len([p for p in productos if p.stock <= p.stock_minimo]),
            "valor_inventario": sum(p.stock * p.precio_compra for p in productos)
        }