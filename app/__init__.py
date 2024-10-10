from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate  # Importa Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()  # Inicializa Migrate
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # Inicializa Flask-Migrate con la app y db
    login_manager.init_app(app)

    from app.routes import auth
    app.register_blueprint(auth.bp)

    return app
