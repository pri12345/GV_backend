from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/static')  # Explicitly set static URL path
    
    # Load configuration
    if config_name == 'development':
        app.config.from_object('config.development.DevelopmentConfig')
    elif config_name == 'production':
        app.config.from_object('config.production.ProductionConfig')
    elif config_name == 'testing':
        app.config.from_object('config.testing.TestingConfig')
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    
    # Register blueprints
    from app.api.v1 import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    # Register root route
    from app.routes import init_app as init_routes
    init_routes(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app 