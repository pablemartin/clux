from peewee import *
from clux.db import ModelBase
from . import user

class ActivityType(ModelBase):
    name = CharField()

class Activity(ModelBase):
    name = CharField()
    type = ForeignKeyField(ActivityType)

class Club(ModelBase):
    name = CharField()
    bio = TextField()
    created_by = ForeignKeyField(user.User)