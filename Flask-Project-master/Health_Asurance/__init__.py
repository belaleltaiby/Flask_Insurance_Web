import os
from flask import Flask
from flask_mysqldb import MySQL


mysql = MySQL()

def create_app():
    # create and configure the app

    app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev'

    )
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] =''
    app.config['MYSQL_DB'] = 'health_insurance'

    mysql = MySQL(app)

    
    
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    return app

