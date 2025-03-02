from flask import Blueprint, redirect, url_for, session, render_template
from app.oauth import oauth

routes = Blueprint('routes', __name__)

@routes.route('/login')
def login():
    google = oauth.create_client('google')
    if not google:
        raise ValueError("Failed to create OAuth client for Google")
    redirect_uri = url_for('routes.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@routes.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    if not google:
        raise ValueError("Failed to create OAuth client for Google")
    # Obtén el token de acceso y la información del usuario
    token = google.authorize_access_token()
    user_info = google.get("userinfo").json()
    # Guarda la información del usuario, incluyendo la foto de perfil
    session['user'] = {
        'name': user_info['name'],
        'email': user_info['email'],
        'picture': user_info['picture'],  # Foto de perfil
    }
    return redirect(url_for('routes.dashboard'))

@routes.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('routes.home'))

@routes.route('/')
def home():
    user = session.get('user')
    if user:
        return redirect(url_for('routes.dashboard'))
    return render_template('index.html', user=user)

@routes.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('routes.login'))
    user = session['user']
    return render_template('dashboard.html', user=user)

@routes.route('/profile')
def profile():
    if 'user' not in session:  # Verifica si el usuario está logueado
        return redirect(url_for('routes.login'))  # Redirige si no está logueado
    user = session['user']  # Recupera el usuario de la sesión
    return render_template('profile.html', user=user)  # Pasa el usuario a la plantilla

@routes.route('/about')
def about():
    return render_template('about.html')

@routes.route('/contact')
def contact():
    return render_template('contact.html')