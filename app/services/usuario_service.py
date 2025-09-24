from app.models.usuario import Usuario, db
from sqlalchemy.exc import IntegrityError


def listar_todos():
    return Usuario.query.all()

def listar_por_id(id):
    return Usuario.query.get(id)

def listar_por_estado(estado):
    return Usuario.query.filter_by(estado=estado).all()


def crear(data):
    # Validar duplicados antes de insertar
    if Usuario.query.filter_by(email=data.get("email")).first():
        raise ValueError("El email ya está registrado")

    if data.get("telefono") and Usuario.query.filter_by(telefono=data.get("telefono")).first():
        raise ValueError("El teléfono ya está registrado")

    if data.get("numero_doc") and Usuario.query.filter_by(
        tipo_doc=data.get("tipo_doc"),
        numero_doc=data.get("numero_doc")
    ).first():
        raise ValueError("El documento ya está registrado")

    usuario = Usuario(**data)
    db.session.add(usuario)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        raise ValueError(f"Error de integridad: {str(e)}")
    return usuario


def editar(id, data):
    usuario = Usuario.query.get(id)
    if not usuario:
        return None

    
    if "email" in data and data["email"] != usuario.email:
        if Usuario.query.filter(Usuario.email == data["email"], Usuario.id != id).first():
            raise ValueError("El email ya está registrado")

    if "telefono" in data and data["telefono"] != usuario.telefono:
        if Usuario.query.filter(Usuario.telefono == data["telefono"], Usuario.id != id).first():
            raise ValueError("El teléfono ya está registrado")

    if "numero_doc" in data and "tipo_doc" in data:
        if (data["numero_doc"] != usuario.numero_doc) or (data["tipo_doc"] != usuario.tipo_doc):
            if Usuario.query.filter(
                Usuario.tipo_doc == data["tipo_doc"],
                Usuario.numero_doc == data["numero_doc"],
                Usuario.id != id
            ).first():
                raise ValueError("El documento ya está registrado")

    
    for key, value in data.items():
        setattr(usuario, key, value)

    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        raise ValueError(f"Error de integridad: {str(e)}")

    return usuario


def eliminar_logico(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return None
    usuario.estado = 0
    db.session.commit()
    return usuario


def restaurar_logico(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return None
    usuario.estado = 1
    db.session.commit()
    return usuario
