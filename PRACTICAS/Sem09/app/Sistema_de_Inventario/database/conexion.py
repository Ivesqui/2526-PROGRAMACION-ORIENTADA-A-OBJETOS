import sqlite3

def conectar():
    """
    Retorna una conexión a la base de datos SQLite.
    Centralizar la conexión permite:
    - Cambiar de BD en el futuro
    - Controlar transacciones
    """
    return sqlite3.connect("inventario.db")


def crear_tablas():
    """
    Crea las tablas necesarias para el sistema.

    Decisión de diseño:
    - Se separa 'productos' de 'movimientos'
    - Los movimientos permiten auditoría y trazabilidad
    """

    conn = conectar()
    cursor = conn.cursor()

    # -------------------------------
    # Tabla productos
    # -------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT UNIQUE NOT NULL,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            stock_minimo INTEGER NOT NULL DEFAULT 5,
            fecha_creacion TEXT NOT NULL,
            fecha_actualizacion TEXT NOT NULL
        )
    """)

    # -------------------------------
    # Tabla movimientos
    # -------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT NOT NULL,
            tipo TEXT NOT NULL, -- ENTRADA / SALIDA / AJUSTE
            cantidad INTEGER NOT NULL,
            motivo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (sku) REFERENCES productos(sku)
        )
    """)

    conn.commit()
    conn.close()

