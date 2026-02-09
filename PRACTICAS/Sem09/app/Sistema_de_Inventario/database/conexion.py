import sqlite3  # Librería estándar de Python para trabajar con bases de datos SQLite


def conectar():
    """
    Establece y retorna una conexión con la base de datos SQLite.

    Decisión de diseño:
    - Se utiliza SQLite porque es una base de datos ligera, no requiere servidor
      y permite persistencia de datos en un solo archivo.
    - La conexión se centraliza en una función para evitar duplicación de código
      y facilitar futuros cambios en la base de datos.
    """
    return sqlite3.connect("inventario.db")


def crear_tabla():
    """
    Crea la tabla 'productos' en la base de datos si no existe.

    Lógica implementada:
    - Se obtiene una conexión a la base de datos.
    - Se crea un cursor para ejecutar sentencias SQL.
    - Se ejecuta una sentencia CREATE TABLE con la cláusula IF NOT EXISTS
      para evitar errores si la tabla ya fue creada previamente.
    - Se confirman los cambios y se cierra la conexión.

    Decisiones de diseño:
    - El campo 'id' es una clave primaria autoincrementable, utilizada como
      identificador técnico interno del sistema.
    - El campo 'sku' es único y obligatorio, y funciona como identificador
      de negocio, permitiendo una gestión más natural para el usuario.
    - Se definen restricciones NOT NULL para asegurar la integridad de los datos.
    - El uso de SQLite garantiza que los datos persistan entre ejecuciones
      del programa sin necesidad de configuraciones adicionales.
    """

    # Se establece la conexión con la base de datos
    conn = conectar()

    # Se crea un cursor que permitirá ejecutar comandos SQL
    cursor = conn.cursor()

    # Sentencia SQL para crear la tabla de productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT UNIQUE NOT NULL,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    """)

    # Se guardan los cambios realizados en la base de datos
    conn.commit()

    # Se cierra la conexión para liberar recursos
    conn.close()

