class InventoryService:
    def __init__(self, repository):
        self.repository = repository

    def register_movement(self, sku, qty, type):
        # 1. Validar stock con el repo
        # 2. Calcular nuevo stock
        # 3. Guardar movimiento
        # 4. Actualizar producto
        pass