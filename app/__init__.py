# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.routes import auth, personas,dashboard  # Asegúrate de que todas las rutas estén importadas aquí
    app.register_blueprint(auth.bp)
    app.register_blueprint(personas.bp)
    app.register_blueprint(dashboard.bp)

    return app
