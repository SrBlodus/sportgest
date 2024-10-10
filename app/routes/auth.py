from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso')  # Mensaje para verificar el inicio de sesión
            return redirect(url_for('auth.dashboard'))  # Redirigir al dashboard
        flash('Credenciales Incorrectas')  # Mensaje de error
    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión con éxito.')  # Mensaje de confirmación de cierre de sesión
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('¡Felicidades, ahora eres un usuario registrado!')  # Mensaje de registro exitoso
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('auth/dashboard.html')  # Página del dashboard
