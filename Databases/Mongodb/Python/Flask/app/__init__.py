from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo() # Initializes the PyMongo object to handle MongoDB operations

def create_app():
    app = Flask(__name__) # Creates instance of the Flask app. __name__ tells Flask where to find the loaction of the application
    app.config.from_object(Config) # Loads the configuration settings from the Config class
    from routes import main
    app.register_blueprint(main) # The main bluprint is imported to allowing for modular routes and views

    return app