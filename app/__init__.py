from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dxcvfdt4w'
    db_path = os.path.abspath(os.path.dirname(__file__))  # Get the directory of the main script
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(db_path, DB_NAME))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    EXCEL_FOLDER = os.path.join(app.root_path, 'static/excel')
    app.config['EXCEL_FOLDER'] = EXCEL_FOLDER
   
    
    db.init_app(app)
    
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True


    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User , List 
    
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')