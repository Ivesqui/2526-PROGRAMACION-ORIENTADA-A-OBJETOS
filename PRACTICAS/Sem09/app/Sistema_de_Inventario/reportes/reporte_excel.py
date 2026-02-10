import sqlite3
import pandas as pd
from datetime import datetime


def generar_excel_inventario(db_path="inventario.db"):
    """
    Genera un archivo Excel con el inventario actual del sistema.

    Enfoque empresarial:
    - Control real de stock
    - Análisis de costos
    - Compatible con Power BI
    - Preparado para histórico y auditoría

    El reporte:
    - Usa solo productos activos
    - Calcula valor del inventario con precio de compra
    - Evalúa estado del stock automáticamente
    """

    # --------------------------------------------------
    # 1. Conexión a la base de datos
    # --------------------------------------------------
    conn = sqlite3.connect(db_path)

    # --------------------------------------------------
    # 2. Consulta SQL alineada al nuevo modelo
    # --------------------------------------------------
    query = """
        SELECT
            sku,
            nombre_producto,
            categoria,
            unidad,
            precio_compra,
            precio_venta,
            stock_actual,
            stock_minimo,
            (stock_actual * precio_compra) AS valor_inventario,
            fecha_creacion,
            fecha_actualizacion
        FROM productos
        WHERE activo = 1
    """

    # Cargar resultados en DataFrame
    df = pd.read_sql_query(query, conn)

    # Cerrar conexión
    conn.close()

    # --------------------------------------------------
    # 3. Regla de negocio: estado del stock
    # --------------------------------------------------
    df["estado_stock"] = df.apply(
        lambda fila: "CRÍTICO"
        if fila["stock_actual"] <= fila["stock_minimo"]
        else "OK",
        axis=1
    )

    # --------------------------------------------------
    # 4. Métricas adicionales útiles para negocio
    # --------------------------------------------------
    df["margen_unitario"] = df["precio_venta"] - df["precio_compra"]
    df["margen_total"] = df["margen_unitario"] * df["stock_actual"]

    # --------------------------------------------------
    # 5. Fecha del reporte (clave para histórico)
    # --------------------------------------------------
    df["fecha_reporte"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --------------------------------------------------
    # 6. Exportación a Excel
    # --------------------------------------------------
    df.to_excel(
        "inventario_emprendimiento.xlsx",
        index=False,
        sheet_name="Inventario"
    )

    print("✅ Excel de inventario generado correctamente")
