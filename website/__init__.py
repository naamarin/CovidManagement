from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = os.getcwd() +"\database.db"

def create_app():
    app = Flask(__name__) #Represent the name of the file that run
    app.config['SECRET_KEY'] = 'FWRG769dbhj890@66' #Encrypt or secure the cookies and session deta related to our website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #My SQLalchemy database is stored at this location
    db.init_app(app) #Initialize the database

    from .member import member #Import the Blueprint member

    app.register_blueprint(member, url_prefix = '/member') #Register the Blueprint member
    #url_prefix = '/' meaning that the prefix off all the blueprints would be '/'

    from .models import Member, Corona, Vaccination
    
    with app.app_context():
        db.create_all()
    
    return app