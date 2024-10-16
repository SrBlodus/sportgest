# app/models/estado_civil.py
from app import db

class EstadoCivil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f'<EstadoCivil {self.nombre}>'
