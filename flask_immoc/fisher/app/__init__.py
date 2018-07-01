from flask import Flask,current_app
import os

def import_from():
    if os.path.exists(os.path.realpath('./app/config/secure.py')):
        return "app.config.secure"
    else:
        return "app.config.setting"

def create_app():
    app = Flask(__name__)
    app.config.from_object(import_from())
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

