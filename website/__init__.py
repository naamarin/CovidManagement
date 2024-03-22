from flask import Flask

def create_app():
    app = Flask(__name__) #represent the name of the file that run
    app.config['SECRET_KEY'] = 'FWRG769dbhj890@66' #encrypt or secure the cookies and session deta related to our website

    from .views import views #import the Blueprint views
    from .auth import auth #import the Blueprint views

    app.register_blueprint(views, url_prefix = '/') #register the Blueprint views
    app.register_blueprint(auth, url_prefix = '/') #register the Blueprint auth
    #url_prefix = '/' meaning that the prefix off all the blueprints would be '/'

    return app