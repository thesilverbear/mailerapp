import mysql.connector 

import click
from flask import current_app, g 
from flask.cli import with_appcontext 
from .schema import instructions 

def get_db():                       
    if 'db' not in g:               
        g.db = mysql.connector.connect(                
            host=current_app.config['DATABASE_HOST'], 
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE'],
            port=current_app.config['DATABASE_PORT']
        ) 
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c 

#función para cerrar db
def close_db(e=None):              #evento = none
    db = g.pop('db', None)
    if db is not None:
        db.close()

#función para ejecutar todas las instrucciones de schema 
def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i) 
    db.commit()  

#crear función que inicialice nuestra db pero que podamos ejecutarla desde la linea de comandos 
# la necesitaremos para crear la db y también para cuando subamos la app a producción

@click.command('init-db')
@with_appcontext 
def init_db_command():  
    init_db()
    click.echo('Base de datos inicializada')

#funcion def init_app(app):

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


