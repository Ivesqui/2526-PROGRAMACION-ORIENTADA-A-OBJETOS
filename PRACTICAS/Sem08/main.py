import os
# Módulo para trabajar con rutas y el sistema operativo
from dashboard_app.dashboard import iniciar_dashboard
# Importa la función principal del dashboard

# Obtiene la ruta absoluta del directorio donde está este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Inicia el dashboard usando el directorio base del proyecto
iniciar_dashboard(BASE_DIR)
