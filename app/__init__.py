import os 
from flask import Flask 

def create_app():       #funcion que se ejecuta siempre en un comienzo con Flask 
    app = Flask(__name__)

    app.config.from_mapping(        #llaves que usaremos dentro de la app
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
        DATABASE_PORT=os.environ.get('FLASK_DATABASE_PORT'),
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY'),
        SECRET_KEY=os.environ.get('SECRET_KEY')
    ) 

    from . import db 

    db.init_app(app)

    from . import mail

    app.register_blueprint(mail.bp)

    return app 



