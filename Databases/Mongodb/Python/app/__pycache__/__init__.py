from flask import Flask
from flask_pymongo import PyMongo
from Python.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from Python.routes import main
    app.register_blueprint(main)

    return app