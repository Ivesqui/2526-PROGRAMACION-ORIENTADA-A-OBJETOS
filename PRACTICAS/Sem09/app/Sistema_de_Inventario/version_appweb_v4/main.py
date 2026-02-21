from infrastructure.repositories.sqlite_producto_repository import SQLiteProductoRepository
from services.inventario_service import InventarioService
from flask import Flask

app = Flask(__name__)

# Configuración de dependencias (Composition Root)
repo = SQLiteProductoRepository()
inventario_service = InventarioService(repo)

# Ahora tus rutas en web/ utilizan inventario_service...