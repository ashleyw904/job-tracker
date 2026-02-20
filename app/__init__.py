from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# Create database and CSRF objects
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # App configuration
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    # Import and register routes
    from app.routes import main
    app.register_blueprint(main)

    # Create database tables
    from app import models
    
    with app.app_context():
        db.create_all()

    return app