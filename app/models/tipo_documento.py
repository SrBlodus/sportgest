# app/models/tipo_documento.py
from app import db

class TipoDocumento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<TipoDocumento {self.nombre}>'
