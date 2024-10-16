# app/decorators.py
from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def role_required(role_names):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role.name not in role_names:
                flash('No tienes permiso para acceder a esta página.')
                return redirect(url_for('auth.login'))  # Redirigir al login si no está autenticado o no tiene el rol adecuado
            return f(*args, **kwargs)
        return decorated_function
    return decorator
