from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    CORS(app)
    
    # Registrar blueprints
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    # Crear tablas de la base de datos
    with app.app_context():
        db.create_all()
    
    return app