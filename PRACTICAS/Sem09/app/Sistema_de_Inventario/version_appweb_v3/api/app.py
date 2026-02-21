from flask import Flask, request, jsonify
from flask_cors import CORS
from database.conexion import crear_tablas
from servicios.inventario import Inventario
from modelos.producto import Producto

app = Flask(__name__)
CORS(app)

# Inicializar BD
crear_tablas()

inventario = Inventario()

# ======================================================
# LISTAR PRODUCTOS
# ======================================================
@app.route("/productos", methods=["GET"])
def listar_productos():
    productos = inventario.listar_productos()

    return jsonify([
        {
            "sku": p.get_sku(),
            "codigo_barras": p.get_codigo_barras(),
            "nombre": p.get_nombre_producto(),
            "categoria": p.get_categoria(),
            "stock": p.get_stock_actual(),
            "precio_venta": p.get_precio_venta(),
            "activo": p.esta_activo()
        }
        for p in productos
    ])


# ======================================================
# BUSCAR PRODUCTO POR SKU
# ======================================================
@app.route("/productos/<sku>", methods=["GET"])
def obtener_producto(sku):
    productos = inventario.buscar_producto(sku)

    if not productos:
        return jsonify({"error": "Producto no encontrado"}), 404

    p = productos[0]

    return jsonify({
        "sku": p.get_sku(),
        "codigo_barras": p.get_codigo_barras(),
        "nombre": p.get_nombre_producto(),
        "categoria": p.get_categoria(),
        "stock": p.get_stock_actual(),
        "precio_venta": p.get_precio_venta(),
        "activo": p.esta_activo()
    })


# ======================================================
# BUSCAR POR CODIGO DE BARRAS (IDEAL ESCANER)
# ======================================================
@app.route("/productos/barcode/<codigo>", methods=["GET"])
def obtener_por_barcode(codigo):
    p = inventario.buscar_por_codigo_barras(codigo)

    if not p:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({
        "sku": p.get_sku(),
        "codigo_barras": p.get_codigo_barras(),
        "nombre": p.get_nombre_producto(),
        "categoria": p.get_categoria(),
        "stock": p.get_stock_actual(),
        "precio_venta": p.get_precio_venta(),
        "activo": p.esta_activo()
    })


# ======================================================
# CREAR PRODUCTO
# ======================================================
@app.route("/productos", methods=["POST"])
def crear_producto():
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
            stock_minimo=int(data["stock_minimo"])
        )

        if inventario.agregar_producto(producto):
            return jsonify({"mensaje": "Producto creado"}), 201
        else:
            return jsonify({"error": "SKU o código ya existe"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ======================================================
# ACTUALIZAR PRODUCTO
# ======================================================
@app.route("/productos/<sku>", methods=["PUT"])
def actualizar_producto(sku):
    data = request.json

    actualizado = inventario.actualizar_producto(
        sku=sku,
        stock=data.get("stock"),
        precio_compra=data.get("precio_compra"),
        precio_venta=data.get("precio_venta"),
        codigo_barras=data.get("codigo_barras")
    )

    if actualizado:
        return jsonify({"mensaje": "Producto actualizado"})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404


# ======================================================
# DESACTIVAR PRODUCTO
# ======================================================
@app.route("/productos/<sku>", methods=["DELETE"])
def eliminar_producto(sku):
    if inventario.desactivar_producto(sku):
        return jsonify({"mensaje": "Producto desactivado"})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)