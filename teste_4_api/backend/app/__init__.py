from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
 
    from .routes import search_blueprint
    app.register_blueprint(search_blueprint)

    return app
