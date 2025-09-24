from flask import Blueprint, request, jsonify
from app.services import usuario_service

usuario_bp = Blueprint("usuario", __name__, url_prefix="/usuarios")

@usuario_bp.get("/")
def get_all():
    usuarios = usuario_service.listar_todos()
    return jsonify([u.to_dict(include_rol=True) for u in usuarios]), 200

@usuario_bp.get("/<int:user_id>")
def get_by_id(user_id):
    usuario = usuario_service.listar_por_id(user_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict(include_rol=True)), 200

@usuario_bp.get("/estado/<int:estado>")
def get_by_estado(estado):
    usuarios = usuario_service.listar_por_estado(estado)
    return jsonify([u.to_dict(include_rol=True) for u in usuarios]), 200

@usuario_bp.post("/")
def create():
    data = request.get_json() or {}
    if "rol_id" not in data:
        return jsonify({"error": "El campo 'rol_id' es requerido"}), 400
    usuario = usuario_service.crear(data)
    return jsonify(usuario.to_dict(include_rol=True)), 201

@usuario_bp.put("/<int:user_id>")
def update(user_id):
    data = request.get_json() or {}
    usuario = usuario_service.editar(user_id, data)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict(include_rol=True)), 200

@usuario_bp.patch("/eliminar/<int:user_id>")
def eliminar(user_id):
    usuario = usuario_service.eliminar_logico(user_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict()), 200

@usuario_bp.patch("/restaurar/<int:user_id>")
def restaurar(user_id):
    usuario = usuario_service.restaurar_logico(user_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict()), 200
