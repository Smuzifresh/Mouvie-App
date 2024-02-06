from flask import Flask
from .extensions import db,login_manager
from config import Config

def create_server():
    app = Flask(__name__,static_url_path="/static")
    app.config.from_object(Config())

    db.init_app(app)
    login_manager.init_app(app)

    from auth import authblp
    from main import mainblp

    app.register_blueprint(authblp)
    app.register_blueprint(mainblp)

    with app.app_context():
        db.create_all()

    return app
