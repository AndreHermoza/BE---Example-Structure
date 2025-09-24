from flask import Blueprint, request, jsonify
from app.services import rol_service

rol_bp = Blueprint("rol", __name__, url_prefix="/roles")

@rol_bp.get("/")
def get_roles():
    roles = rol_service.listar_todos()
    return jsonify([r.to_dict() for r in roles]), 200

@rol_bp.get("/<int:rol_id>")
def get_rol(rol_id):
    rol = rol_service.listar_por_id(rol_id)
    if not rol:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify(rol.to_dict()), 200

@rol_bp.post("/")
def create_rol():
    data = request.get_json() or {}
    if "rol" not in data:
        return jsonify({"error": "El campo 'rol' es requerido"}), 400
    nuevo = rol_service.crear(data)
    return jsonify(nuevo.to_dict()), 201

@rol_bp.put("/<int:rol_id>")
def update_rol(rol_id):
    data = request.get_json() or {}
    rol = rol_service.editar(rol_id, data)
    if not rol:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify(rol.to_dict()), 200

@rol_bp.patch("/eliminar/<int:rol_id>")
def delete_rol(rol_id):
    rol = rol_service.eliminar(rol_id)
    if not rol:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify(rol.to_dict()), 200

@rol_bp.patch("/restaurar/<int:rol_id>")
def restore_rol(rol_id):
    rol = rol_service.restaurar(rol_id)
    if not rol:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify(rol.to_dict()), 200
