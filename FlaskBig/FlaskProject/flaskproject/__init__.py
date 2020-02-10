from flask import Flask

def create_app():
    app = Flask (__name__)
    app.config['SECRET_KEY']='jghsjhgjsdhgjshgjksh'
    return app
from flaskproject import routes
