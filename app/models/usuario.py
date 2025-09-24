from app import db
from sqlalchemy.sql import func

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    rol_id = db.Column(db.Integer, db.ForeignKey("rol.id"), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    tipo_doc = db.Column(db.String(3), nullable=False)
    numero_doc = db.Column(db.String(20), unique=True, nullable=False)
    telefono = db.Column(db.String(9))
    email = db.Column(db.String(200), unique=True, nullable=False)
    contrasenia = db.Column(db.String(220), nullable=False)
    registro = db.Column(db.TIMESTAMP, server_default=func.current_timestamp())
    estado = db.Column(db.SmallInteger, default=1)

    def to_dict(self, include_rol: bool = False):
        d = {
            "id": self.id,
            "rol_id": self.rol_id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "tipo_doc": self.tipo_doc,
            "numero_doc": self.numero_doc,
            "telefono": self.telefono,
            "email": self.email,
            "contrasenia": self.contrasenia,
            "registro": str(self.registro) if self.registro else None,
            "estado": int(self.estado) if self.estado is not None else None,
        }
        if include_rol and self.rol:
            d["rol"] = self.rol.to_dict()
        return d
