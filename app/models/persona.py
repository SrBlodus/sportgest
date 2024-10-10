# app/models/persona.py
from app import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    correo = db.Column(db.String(128), unique=True, nullable=False)
    direccion = db.Column(db.String(256), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)

    # Relación con el modelo User
    usuario = db.relationship('User', backref='persona', uselist=False)

    def __repr__(self):
        return f'<Persona {self.nombre}>'
