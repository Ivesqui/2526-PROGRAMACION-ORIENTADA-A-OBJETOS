from functools import wraps
from flask import request
from security.jwt_utils import verificar_token


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return {"error": "Token requerido"}, 401

        if not auth_header.startswith("Bearer "):
            return {"error": "Formato de token inválido"}, 401

        try:
            token = auth_header.split(" ")[1]
            decoded = verificar_token(token)
            request.user = decoded
        except Exception:
            return {"error": "Token inválido"}, 401

        return f(*args, **kwargs)

    return decorated