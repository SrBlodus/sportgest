import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'mysql://aabr:031297.Ale@localhost/sportgest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False