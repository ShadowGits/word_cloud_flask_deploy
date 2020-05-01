from flask import Flask

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from models import db
    db.init_app(app)

    return app
