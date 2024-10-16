# app/models/sexo.py
from app import db

class Sexo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'<Sexo {self.nombre}>'
