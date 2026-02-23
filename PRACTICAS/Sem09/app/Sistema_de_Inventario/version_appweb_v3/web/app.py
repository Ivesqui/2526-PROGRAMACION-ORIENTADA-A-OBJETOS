# ======================================================
# API WEB - SISTEMA DE INVENTARIO
# ======================================================

from flask import Flask, request, jsonify
from flask_cors import CORS

from core.entities.producto import Producto
from services.inventario_service import InventarioService
from services.sqlite_producto_repository import SqliteProductoRepository

# ======================================================
# CONFIGURACIÓN
# ======================================================

app = Flask(__name__)
CORS(app)

repo = SqliteProductoRepository()
inventario = InventarioService(repo)


# ======================================================
# RESPUESTAS ESTÁNDAR
# ======================================================

def success_response(data=None, message=None, status=200):
    response = {}
    if message:
        response["message"] = message
    if data is not None:
        response["data"] = data
    return jsonify(response), status


def error_response(message, status=400):
    return jsonify({"error": message}), status


# ======================================================
# PRODUCTOS
# ======================================================

# ✔ Crear producto
@app.route("/productos", methods=["POST"])
def crear_producto():
    try:
        data = request.get_json()

        producto = Producto(
            sku=data["sku"],
            codigo_barras=data.get("codigo_barras"),
            nombre_producto=data["nombre_producto"],
            categoria=data["categoria"],
            descripcion=data.get("descripcion"),
            unidad=data["unidad"],
            precio_compra=float(data["precio_compra"]),
            precio_venta=float(data["precio_venta"]),
            stock_actual=int(data["stock_actual"]),
            stock_minimo=int(data["stock_minimo"]),
            activo=True
        )

        inventario.crear_producto(producto)

        return success_response(message="Producto creado", status=201)

    except ValueError as e:
        return error_response(str(e), 400)

    except Exception:
        return error_response("Error interno del servidor", 500)


# ✔ Listar todos / activos
@app.route("/productos", methods=["GET"])
def listar_productos():

    estado = request.args.get("estado")  # ACTIVO / INACTIVO

    productos = inventario.listar_productos(estado)

    return success_response(data=productos)


# ✔ Buscar por SKU
@app.route("/productos/<sku>", methods=["GET"])
def buscar_por_sku(sku):

    producto = inventario.buscar_por_sku(sku)

    if not producto:
        return error_response("Producto no encontrado", 404)

    return success_response(data=producto)


# ✔ Buscar por nombre
@app.route("/productos/nombre/<nombre>", methods=["GET"])
def buscar_por_nombre(nombre):

    productos = inventario.buscar_por_nombre(nombre)

    return success_response(data=productos)


# ✔ Buscar por código de barras
@app.route("/productos/barcode/<codigo>", methods=["GET"])
def buscar_por_codigo(codigo):

    producto = inventario.buscar_por_codigo_barras(codigo)

    if not producto:
        return error_response("Producto no encontrado", 404)

    return success_response(data=producto)


# ✔ PUT total
@app.route("/productos/<sku>", methods=["PUT"])
def actualizar_total(sku):

    data = request.get_json()

    actualizado = inventario.actualizar_producto(sku, data)

    if not actualizado:
        return error_response("Producto no encontrado", 404)

    return success_response(message="Producto actualizado")


# ✔ PATCH parcial
@app.route("/productos/<sku>", methods=["PATCH"])
def actualizar_parcial(sku):

    data = request.get_json()

    actualizado = inventario.actualizar_parcial(sku, data)

    if not actualizado:
        return error_response("Producto no encontrado", 404)

    return success_response(message="Producto actualizado parcialmente")

# ✔ PATCH alta lógica
@app.route("/productos/<sku>/alta", methods=["PATCH"])
def dar_de_alta(sku):

    activado = inventario.activar_producto(sku)

    if not activado:
        return error_response("Producto no encontrado", 404)

    return success_response(message="Producto activado")

# ✔ PATCH baja lógica
@app.route("/productos/<sku>/baja", methods=["PATCH"])
def dar_de_baja(sku):

    eliminado = inventario.desactivar_producto(sku)

    if not eliminado:
        return error_response("Producto no encontrado", 404)

    return success_response(message="Producto desactivado")


# ======================================================
# MOVIMIENTOS
# ======================================================

# ✔ Registrar movimiento
@app.route("/movimientos", methods=["POST"])
def registrar_movimiento():

    try:
        data = request.get_json()

        resultado = inventario.registrar_movimiento(
            sku=data["sku"],
            tipo=data["tipo"],
            cantidad=int(data["cantidad"]),
            motivo=data.get("motivo", "")
        )

        if not resultado:
            return error_response("Producto no encontrado", 404)

        return success_response(message="Movimiento registrado")

    except ValueError as e:
        return error_response(str(e), 400)

    except Exception:
        return error_response("Error interno del servidor", 500)


# ✔ Ver Kardex
@app.route("/productos/<sku>/movimientos", methods=["GET"])
def ver_movimientos(sku):

    movimientos = inventario.obtener_movimientos_por_sku(sku)

    return success_response(data=movimientos)


# ======================================================
# DASHBOARD
# ======================================================

@app.route("/dashboard/resumen", methods=["GET"])
def dashboard():

    resumen = inventario.obtener_resumen_dashboard()

    return success_response(data=resumen)


# ======================================================
# PRODUCCIÓN
# ======================================================

if __name__ == "__main__":
    # Para desarrollo únicamente
    app.run(host="0.0.0.0", port=5000)