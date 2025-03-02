from flask import Flask
from app.oauth import init_oauth
from app.routes import routes
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Initialize OAuth
init_oauth(app)

# Register blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)