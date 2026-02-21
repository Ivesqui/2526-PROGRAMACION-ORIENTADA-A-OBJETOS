import sqlite3


def conectar():
    """
    Establece y retorna una conexión a la base de datos SQLite.

    Decisión de diseño:
    - SQLite es suficiente para un emprendimiento pequeño o mediano.
    - No requiere servidor.
    - Permite trabajar con archivos (inventario.db).
    """
    return sqlite3.connect("inventario.db")


def crear_tablas():
    """
    Crea las tablas necesarias para el sistema de inventario.

    Diseño del sistema:
    - Se separa la información del producto (tabla productos)
      del historial de movimientos (tabla movimientos).
    - Esto permite trazabilidad, auditoría y reportes.
    """

    conn = conectar()
    cursor = conn.cursor()

    # ==========================================================
    # TABLA: productos
    # ==========================================================
    """
    Representa el estado actual del inventario.

    Campos clave:
    - sku: identificador de negocio (no técnico)
    - precio_compra / precio_venta: permiten calcular márgenes
    - stock_actual / stock_minimo: permiten alertas
    - activo: permite desactivar productos sin eliminarlos
    """

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT UNIQUE NOT NULL,
            codigo_barras TEXT UNIQUE,
            nombre_producto TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descripcion TEXT,
            unidad TEXT NOT NULL,
            precio_compra REAL NOT NULL,
            precio_venta REAL NOT NULL,
            stock_actual INTEGER NOT NULL,
            stock_minimo INTEGER NOT NULL,
            activo INTEGER NOT NULL DEFAULT 1,
            fecha_creacion TEXT NOT NULL,
            fecha_actualizacion TEXT NOT NULL
        )
    """)

    # ==========================================================
    # TABLA: movimientos
    # ==========================================================
    """
    Registra cada cambio de stock.

    Esta tabla NO representa el estado actual,
    sino el HISTORIAL del inventario.

    Campos importantes:
    - tipo: ENTRADA / SALIDA / AJUSTE
    - motivo: explica por qué ocurrió el movimiento
    - fecha: permite auditoría y reportes
    """

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT NOT NULL,
            tipo TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            motivo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (sku) REFERENCES productos(sku)
        )
    """)

    conn.commit()
    conn.close()

