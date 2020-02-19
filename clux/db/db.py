import os
import click
from flask.cli import with_appcontext
from flask.cli import AppGroup
from peewee import *
from config import Config

# import peeweedbevolve

if os.environ.get("FLASK_ENV") == 'development':
    db = SqliteDatabase('clux.db')
else:
    db = PostgresqlDatabase(
        Config.DATABASE['name'], 
        user=Config.DATABASE['user'], 
        host=Config.DATABASE['host'], 
        password=Config.DATABASE['password']
    )

class ModelBase(Model):
    class Meta:
        database = db