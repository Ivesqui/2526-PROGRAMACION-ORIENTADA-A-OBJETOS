import sqlite3
import pandas as pd
from datetime import datetime

def generar_excel_inventario(db_path="inventario.db"):
    """
    Genera un archivo Excel con el inventario actual del sistema.

    Este reporte está diseñado con enfoque empresarial:
    - Puede ser consumido directamente por Power BI
    - Sirve para análisis de stock, costos y toma de decisiones
    - No contiene formatos visuales, solo datos estructurados

    Decisiones de diseño:
    - Se consulta directamente la base de datos para evitar duplicar lógica
    - Se calculan métricas clave (valor_total, estado_stock)
    - Se agrega una marca temporal para permitir análisis histórico
    """

    # --------------------------------------------------
    # 1. Conexión a la base de datos SQLite
    # --------------------------------------------------
    conn = sqlite3.connect(db_path)

    # --------------------------------------------------
    # 2. Consulta SQL orientada a negocio
    #    (no solo datos crudos)
    # --------------------------------------------------
    query = """
        SELECT
            sku,
            nombre,
            cantidad,
            precio AS precio_unitario,
            cantidad * precio AS valor_total,
            5 AS stock_minimo
        FROM productos
    """

    # Se carga el resultado directamente en un DataFrame
    df = pd.read_sql_query(query, conn)

    # Cerramos la conexión para liberar recursos
    conn.close()

    # --------------------------------------------------
    # 3. Regla de negocio: estado del stock
    # --------------------------------------------------
    df["estado_stock"] = df.apply(
        lambda fila: "BAJO" if fila["cantidad"] <= fila["stock_minimo"] else "OK",
        axis=1
    )

    # --------------------------------------------------
    # 4. Fecha del reporte (clave para histórico y BI)
    # --------------------------------------------------
    df["fecha_reporte"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --------------------------------------------------
    # 5. Exportación a Excel
    # --------------------------------------------------
    df.to_excel(
        "inventario_emprendimiento.xlsx",
        index=False,
        sheet_name="Inventario"
    )

    print("✅ Excel de inventario generado correctamente")
