
from flask import Flask
from .extensions import db
from .config import Config
from .models import Usuario
from sqlalchemy import inspect
from .routes import api as api_routes

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.register_blueprint(api_routes)
    db.init_app(app)
    return app

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        verificar_db = inspect(db.engine)
        if not verificar_db.get_table_names():
            db.create_all()
    app.run(debug=True)




