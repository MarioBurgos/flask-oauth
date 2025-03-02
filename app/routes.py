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
    token = google.authorize_access_token()
    user_info = google.get("userinfo").json()
    session['user'] = user_info
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
    user = session.get('user')
    if not user:
        return redirect(url_for('routes.home'))
    return render_template('dashboard.html', user=user)