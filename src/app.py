
from flask import Flask

from .config import db



def create_app():
    app = Flask(__name__, instance_relative_config=True)
    from .config import Config
    app.config.from_object(Config)
    from .models import Usuario
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app





