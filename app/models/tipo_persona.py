# app/models/tipo_persona.py
from app import db

# Tabla de asociación para la relación muchos a muchos entre Personas y Tipos de Personas
persona_x_tipo = db.Table('persona_x_tipo',
    db.Column('persona_id', db.Integer, db.ForeignKey('persona.id'), primary_key=True),
    db.Column('tipo_persona_id', db.Integer, db.ForeignKey('tipo_persona.id'), primary_key=True)
)

# Modelo para los Tipos de Persona
class TipoPersona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f'<TipoPersona {self.nombre}>'
