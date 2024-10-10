# run.py
from app import create_app, db
from app.models.user import User
from app.models.persona import Persona
from app.models.role import Role

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

    # Verificar si ya existe la persona admin
    persona_admin = Persona.query.filter_by(nombre='admin').first()
    if not persona_admin:
        persona_admin = Persona(nombre='admin', correo='admin@admin.com', direccion='Calle Falsa 123', telefono='123456789')
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
