# app/routes/dashboard.py
from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
@login_required  # Asegúrate de que el usuario esté autenticado
def dashboard():
    return render_template('auth/dashboard.html')
