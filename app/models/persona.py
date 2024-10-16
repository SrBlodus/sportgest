# app/models/persona.py
from datetime import datetime

from app import db
from app.models.tipo_persona import persona_x_tipo  # Asegúrate de que esta relación esté bien importada
from app.models.tipo_documento import TipoDocumento  # Importa el modelo TipoDocumento
from app.models.sexo import Sexo  # Importa el modelo Sexo
from app.models.nacionalidad import Nacionalidad  # Importa el modelo Nacionalidad
from app.models.estado_civil import EstadoCivil  # Importa el modelo EstadoCivil

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    apellidos = db.Column(db.String(128), nullable=False)  # Nuevo campo para apellidos
    direccion = db.Column(db.String(256), nullable=True)
    ciudad = db.Column(db.String(128), nullable=True)  # Nuevo campo para ciudad
    barrio = db.Column(db.String(128), nullable=True)  # Nuevo campo para barrio
    numero_documento = db.Column(db.String(50), unique=True, nullable=True)  # Nuevo campo para número de documento
    tipo_documento_id = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'))  # Relación con tipo de documento
    sexo_id = db.Column(db.Integer, db.ForeignKey('sexo.id'))  # Relación con sexo
    nacionalidad_id = db.Column(db.Integer, db.ForeignKey('nacionalidad.id'))  # Relación con nacionalidad
    estado_civil_id = db.Column(db.Integer, db.ForeignKey('estado_civil.id'))  # Relación con estado civil
    correo = db.Column(db.String(128), unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=True)  # Nuevo campo para fecha de nacimiento
    telefono = db.Column(db.String(20), nullable=True)

    # Relación con el modelo User
    usuario = db.relationship('User', backref='persona', uselist=False)
    # Relación muchos a muchos con TipoPersona, usando la tabla intermedia persona_x_tipo
    tipos = db.relationship('TipoPersona', secondary=persona_x_tipo, backref='personas')

    # Relaciones con otros modelos
    tipo_documento = db.relationship('TipoDocumento', backref='personas', lazy=True)
    sexo = db.relationship('Sexo', backref='personas', lazy=True)
    nacionalidad = db.relationship('Nacionalidad', backref='personas', lazy=True)
    estado_civil = db.relationship('EstadoCivil', backref='personas', lazy=True)

    def __repr__(self):
        return f'<Persona {self.nombre} {self.apellidos}>'

    def edad(self):
        if self.fecha_nacimiento:
            return (datetime.date.today() - self.fecha_nacimiento).days // 365
        return None
