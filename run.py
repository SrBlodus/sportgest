# run.py
from app import create_app, db
from app.models.user import User

app = create_app()

# Crear tablas y añadir usuario admin si no existe
with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos

    # Verificar si ya existe el usuario admin
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        # Si no existe, crear el usuario admin
        admin_user = User(username='admin')
        admin_user.set_password('admin')  # Cambia 'admin_password' por la contraseña que desees
        db.session.add(admin_user)
        db.session.commit()
        print("Usuario admin creado.")

if __name__ == '__main__':
    app.run(debug=True)
