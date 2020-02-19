import click
from playhouse.migrate import *
from flask.cli import with_appcontext
from flask.cli import AppGroup
from clux.db import db
from clux.models import *

import os

if os.environ.get("FLASK_ENV") == 'development':
    migrator = SqliteMigrator(db)
else:
    migrator = PostgresqlMigrator(db)

db_cli = AppGroup('db')

@db_cli.command('migrate')
def migrate_db():

    db.connect()
    db.create_tables([
        Club,
        Activity,
        ActivityType,
        User
    ])

    # Migraciones con peewee
    # https://github.com/keredson/peewee-db-evolve
    # db.evolve()