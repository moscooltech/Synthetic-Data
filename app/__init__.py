import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app import models
    
    from app.blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.blueprints.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from app.blueprints.generator import generator as generator_blueprint
    app.register_blueprint(generator_blueprint, url_prefix='/generator')
    
    return app
