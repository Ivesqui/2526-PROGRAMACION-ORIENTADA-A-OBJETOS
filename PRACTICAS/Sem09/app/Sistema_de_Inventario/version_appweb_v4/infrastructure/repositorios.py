class SQLiteProductRepository:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_by_sku(self, sku):
        # SOLO el SELECT aquí
        pass

    def update_stock(self, sku, new_stock):
        # SOLO el UPDATE aquí
        pass