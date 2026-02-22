# ======================================================
# IMPORTACIONES
# ======================================================

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

# Entidad de dominio (NO depende de Flask ni SQLite)
from core.entities.producto import Producto

# Capa de servicios (lógica de negocio)
from services.inventario_service import InventarioService

# Implementación concreta de base de datos SQLite
from services.sqlite_producto_repository import (
    SqliteProductoRepository
)

# Inicialización de Flask
app = Flask(__name__)

# Permitir peticiones desde frontend (React, Vue, etc.)
CORS(app)

# ======================================================
# INYECCIÓN DE DEPENDENCIAS
# ======================================================

# Creamos el repositorio SQLite
repo = SqliteProductoRepository()

# Inyectamos el repositorio al servicio
inventario = InventarioService(repo)


# ======================================================
# LISTAR PRODUCTOS
# ======================================================
@app.route("/productos", methods=["GET"])
def listar_productos():
    """
    Devuelve todos los productos activos.
    """

    productos = inventario.listar_productos()


    return jsonify([p.to_dict() for p in productos])

# ======================================================
# OBTENER PRODUCTO POR SKU
# ======================================================
@app.route("/productos/<sku>", methods=["GET"])
def obtener_producto(sku):
    """
    Devuelve un producto específico por su SKU.
    """

    producto = inventario.buscar_producto_por_sku(sku)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify(producto.to_dict())


# ======================================================
# BUSCAR POR NOMBRE
# ======================================================
@app.route("/productos/nombre/<nombre>", methods=["GET"])
def buscar_por_nombre(nombre):
    """
    Busca productos que coincidan con el nombre.
    """

    productos = inventario.buscar_por_nombre(nombre)

    return jsonify([p.to_dict() for p in productos])


# ======================================================
# BUSCAR POR CÓDIGO DE BARRAS
# ======================================================
@app.route("/productos/barcode/<codigo>", methods=["GET"])
def buscar_por_codigo(codigo):
    """
    Busca producto por código de barras.
    """

    producto = inventario.buscar_por_codigo_barras(codigo)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify(producto.to_dict())


# ======================================================
# CREAR PRODUCTO
# ======================================================
@app.route("/productos", methods=["POST"])
def crear_producto():
    """
    Crea un nuevo producto en el inventario.
    """

    data = request.json

    try:
        producto = Producto(
            sku=data["sku"],
            codigo_barras=data.get("codigo_barras"),
            nombre_producto=data["nombre_producto"],
            categoria=data["categoria"],
            unidad=data["unidad"],
            precio_compra=float(data["precio_compra"]),
            precio_venta=float(data["precio_venta"]),
            stock_actual=int(data["stock_actual"]),
            stock_minimo=int(data["stock_minimo"]),
            activo=True
        )

        creado = inventario.agregar_producto(producto)

        if not creado:
            return jsonify({"error": "SKU o código ya existe"}), 400

        return jsonify({"mensaje": "Producto creado"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ======================================================
# ACTUALIZACIÓN TOTAL (PUT)
# ======================================================
@app.route("/productos/<sku>", methods=["PUT"])
def actualizar_producto(sku):
    """
    Actualiza completamente un producto.
    """

    data = request.json

    actualizado = inventario.actualizar_producto(
        sku=sku,
        datos=data
    )

    if not actualizado:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Producto actualizado"})


# ======================================================
# ACTUALIZACIÓN PARCIAL (PATCH)
# ======================================================
@app.route("/productos/<sku>", methods=["PATCH"])
def actualizar_parcial(sku):
    """
    Actualiza solo algunos campos del producto.
    """

    data = request.json

    actualizado = inventario.actualizar_parcial(sku, data)

    if not actualizado:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Producto actualizado parcialmente"})


# ======================================================
# DAR DE BAJA
# ======================================================
@app.route("/productos/<sku>/baja", methods=["PATCH"])
def dar_de_baja(sku):
    """
    Desactiva un producto (borrado lógico).
    """

    eliminado = inventario.desactivar_producto(sku)

    if not eliminado:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Producto desactivado"})


# ======================================================
# REGISTRAR MOVIMIENTO
# ======================================================
@app.route("/movimientos", methods=["POST"])
def crear_movimiento():
    """
    Registra entrada o salida de inventario.
    """

    data = request.json

    try:
        resultado = inventario.registrar_movimiento(
            sku=data["sku"],
            tipo=data["tipo"],
            cantidad=int(data["cantidad"]),
            motivo=data.get("motivo", "")
        )

        if not resultado:
            return jsonify({"error": "Producto no encontrado"}), 404

        return jsonify({"mensaje": "Movimiento registrado correctamente"})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# ======================================================
# VER KARDEX
# ======================================================
@app.route("/productos/<sku>/movimientos", methods=["GET"])
def obtener_movimientos(sku):
    """
    Devuelve todos los movimientos de un producto.
    """

    movimientos = inventario.obtener_movimientos_por_sku(sku)
    return jsonify(movimientos)


# ======================================================
# DASHBOARD
# ======================================================
@app.route("/dashboard/resumen", methods=["GET"])
def resumen_dashboard():
    """
    Devuelve métricas generales del inventario.
    """

    resumen = inventario.obtener_resumen_dashboard()
    return jsonify(resumen)


# ======================================================
# EJECUCIÓN
# ======================================================
if __name__ == "__main__":
    app.run(debug=True)