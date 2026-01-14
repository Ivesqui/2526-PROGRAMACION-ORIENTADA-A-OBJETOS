# ================================
# Exportador a Excel
# ================================
# Usa pandas para guardar la información en un archivo Excel

import pandas as pd

def exportar_a_excel(resumen, nombre_archivo="servicios.xlsx"):
    df = pd.DataFrame(resumen)
    df.to_excel(nombre_archivo, index=False)
