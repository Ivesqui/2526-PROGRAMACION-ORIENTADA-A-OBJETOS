from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from reportes.reporte_excel import generar_excel_inventario_en_memoria
from database.conexion import crear_tablas
from servicios.inventario import Inventario
from modelos.producto import Producto

app = Flask(__name__)
CORS(app)

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
# BUSCAR POR NOMBRE
# ======================================================
@app.route("/productos/nombre/<nombre>", methods=["GET"])
def buscar_por_nombre(nombre):
    productos = inventario.buscar_por_nombre(nombre)

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
# BUSCAR POR CÓDIGO DE BARRAS
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
# ACTUALIZAR TOTALMENTE
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
# ACTUALIZAR PARCIAL
# ======================================================
@app.route("/productos/<sku>", methods=["PATCH"])
def actualizar_parcial(sku):
    data = request.json

    actualizado = inventario.actualizar_parcial(sku, data)

    if actualizado:
        return jsonify({"mensaje": "Producto actualizado parcialmente"})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404


# ======================================================
# DAR DE BAJA
# ======================================================
@app.route("/productos/<sku>/baja", methods=["PATCH"])
def dar_de_baja(sku):
    if inventario.desactivar_producto(sku):
        return jsonify({"mensaje": "Producto desactivado"})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404


# ======================================================
# REGISTRAR MOVIMIENTO
# ======================================================
@app.route("/movimientos", methods=["POST"])
def crear_movimiento():
    data = request.json

    try:
        producto = inventario.registrar_movimiento(
            sku=data["sku"],
            tipo=data["tipo"],
            cantidad=int(data["cantidad"]),
            motivo=data.get("motivo", "")
        )

        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        return jsonify({"mensaje": "Movimiento registrado correctamente"})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# ======================================================
# VER KARDEX
# ======================================================
@app.route("/productos/<sku>/movimientos", methods=["GET"])
def obtener_movimientos(sku):
    movimientos = inventario.obtener_movimientos_por_sku(sku)
    return jsonify(movimientos)


# ======================================================
# DASHBOARD
# ======================================================
@app.route("/dashboard/resumen", methods=["GET"])
def resumen_dashboard():
    productos = inventario.listar_productos()

    total = len(productos)

    criticos = [
        p for p in productos
        if p.get_stock_actual() <= p.get_stock_minimo()
    ]

    valor_total = sum(
        p.get_stock_actual() * p.get_precio_compra()
        for p in productos
    )

    return jsonify({
        "total_productos": total,
        "productos_criticos": len(criticos),
        "valor_total_inventario": valor_total
    })


# ======================================================
# REPORTE EXCEL
# ======================================================
@app.route("/reportes/inventario/excel", methods=["GET"])
def descargar_excel():
    archivo = generar_excel_inventario_en_memoria()

    return send_file(
        archivo,
        as_attachment=True,
        download_name="inventario_emprendimiento.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


if __name__ == "__main__":
    app.run(debug=True)

