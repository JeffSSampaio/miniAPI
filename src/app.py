
from flask import Flask
from .extensions import db
from .config import Config
from .models import Usuario
from sqlalchemy import inspect

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app




