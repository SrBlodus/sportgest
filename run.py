# run.py
from app import create_app, db
from app.models.user import User
from app.models.persona import Persona
from app.models.role import Role
from app.models.tipo_persona import TipoPersona
from app.models.tipo_documento import TipoDocumento
from app.models.sexo import Sexo
from app.models.nacionalidad import Nacionalidad
from app.models.estado_civil import EstadoCivil

app = create_app()

with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos

    # Crear roles si no existen
    roles = ['admin', 'operador', 'tutor', 'alumno', 'profesor']
    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            role = Role(name=role_name)
            db.session.add(role)
            print(f"Rol '{role_name}' creado.")
    db.session.commit()

    # Crear tipos de documentos si no existen
    tipos_documento = ['Cédula de Identidad Nacional', 'Pasaporte', 'Documento Extranjero']
    for valor in tipos_documento:
        tipo_documento = TipoDocumento.query.filter_by(nombre=valor).first()
        if not tipo_documento:
            tipo_documento = TipoDocumento(nombre=valor)
            db.session.add(tipo_documento)
            print(f"Tipo de documento '{valor}' creado.")

    # Crear sexos si no existen
    sexos = ['Masculino', 'Femenino', 'Otro']
    for valor in sexos:
        sexo = Sexo.query.filter_by(nombre=valor).first()
        if not sexo:
            sexo = Sexo(nombre=valor)
            db.session.add(sexo)
            print(f"Sexo '{valor}' creado.")

    # Crear nacionalidades si no existen
    nacionalidades = ['Paraguaya', 'Argentina', 'Brasileña', 'Uruguaya', 'Boliviana', 'Alemana']
    for valor in nacionalidades:
        nacionalidad = Nacionalidad.query.filter_by(nombre=valor).first()
        if not nacionalidad:
            nacionalidad = Nacionalidad(nombre=valor)
            db.session.add(nacionalidad)
            print(f"Nacionalidad '{valor}' creada.")

    # Crear estados civiles si no existen
    estados_civiles = ['Soltero', 'Casado', 'Divorciado', 'Viudo', 'En pareja']
    for valor in estados_civiles:
        estado_civil = EstadoCivil.query.filter_by(nombre=valor).first()
        if not estado_civil:
            estado_civil = EstadoCivil(nombre=valor)
            db.session.add(estado_civil)
            print(f"Estado civil '{valor}' creado.")

    db.session.commit()

    # Verificar si ya existe la persona admin
    persona_admin = Persona.query.filter_by(nombre='admin').first()
    if not persona_admin:
        persona_admin = Persona(nombre='admin', apellidos='admin', correo='admin@admin.com',
                                direccion='Calle Falsa 123', telefono='123456789')
        db.session.add(persona_admin)
        db.session.commit()
        print("Persona admin creada.")

    # Verificar si ya existe el usuario admin
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        admin_user = User(username='admin')
        admin_user.set_password('admin')
        admin_user.role_id = Role.query.filter_by(name='admin').first().id  # Asigna el rol de admin
        db.session.add(admin_user)
        db.session.commit()
        print("Usuario admin creado.")
    else:
        print("Usuario admin ya existe.")

    # Vincular la persona admin con el usuario admin
    if admin_user and not admin_user.persona_id:
        admin_user.persona_id = persona_admin.id
        db.session.commit()
        print("Usuario admin vinculado a la persona admin.")

if __name__ == '__main__':
    app.run(debug=True)
