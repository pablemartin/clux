import datetime
import wtforms
from peewee import *
from clux.db import ModelBase
from flask_security import UserMixin, RoleMixin

class PasswordField(TextField):
    def wtf_field(self, model, **kwargs):
        return wtforms.PasswordField(**kwargs)

class Role(ModelBase, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)

class User(ModelBase, UserMixin):
    username = CharField(null=True)
    name = CharField(null=True)
    email = TextField()
    password = PasswordField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    updated_date = DateTimeField(null=True)

    def __str__(self):
        return self.username

class UserRoles(ModelBase):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)
    created_date = DateTimeField(default=datetime.datetime.now)
    updated_date = DateTimeField(null=True)