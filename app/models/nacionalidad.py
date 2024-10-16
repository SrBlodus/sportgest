# app/models/nacionalidad.py
from app import db

class Nacionalidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Nacionalidad {self.nombre}>'
