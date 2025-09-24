from app import db

class Rol(db.Model):
    __tablename__ = "rol"

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.SmallInteger, default=1)

    # relación inversa con usuario
    usuarios = db.relationship("Usuario", backref="rol", lazy="select")

    def to_dict(self):
        return {
            "id": self.id,
            "rol": self.rol,
            "estado": self.estado
        }
