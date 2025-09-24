from app import db
from app.models.rol import Rol

def listar_todos():
    return Rol.query.all()

def listar_por_id(rol_id):
    return Rol.query.get(rol_id)

def crear(data):
    nuevo = Rol(rol=data["rol"], estado=data.get("estado", 1))
    db.session.add(nuevo)
    db.session.commit()
    db.session.refresh(nuevo)
    return nuevo

def editar(rol_id, data):
    rol = listar_por_id(rol_id)
    if not rol:
        return None
    if "rol" in data:
        rol.rol = data["rol"]
    if "estado" in data:
        rol.estado = data["estado"]
    db.session.commit()
    db.session.refresh(rol)
    return rol

def eliminar(rol_id):
    rol = listar_por_id(rol_id)
    if not rol:
        return None
    rol.estado = 0
    db.session.commit()
    return rol

def restaurar(rol_id):
    rol = listar_por_id(rol_id)
    if not rol:
        return None
    rol.estado = 1
    db.session.commit()
    db.session.refresh(rol)
    return rol
