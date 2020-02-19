import os.path as op
from flask import Blueprint
from flask import request
from flask import session
from flask import render_template
from flask import url_for
from flask import redirect
from flask_admin import *
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.base import MenuLink
from flask_admin.contrib.peewee import ModelView
import flask_login
from clux.models import *

# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):
#     """
#     TODO: self login/registration views
#     """
#     @expose('/')
#     def index(self):
#         if not flask_login.current_user.is_authenticated:
#             return redirect(url_for('security.login', next=request.url))
#         return super(MyAdminIndexView, self).index()
    pass

class ModelViewBase(ModelView):
    # def is_accessible(self):
    #     return flask_login.current_user.is_authenticated

    # def inaccessible_callback(self, name, **kwargs):
    #     # redirect to login page if user doesn't have access
    #     return redirect(url_for('security.login', next=request.url))
    pass

class UserAdmin(ModelViewBase): pass
class UserRoleAdmin(ModelViewBase): pass
class UserRolesAdmin(ModelViewBase): pass
class RoleAdmin(ModelViewBase): pass

class AdminManager():

    def __init__(self, app):
        self.admin = Admin(app, name='clux', index_view=MyAdminIndexView())
        
        self.admin.add_sub_category(name="Administrador", parent_name='clux')
        self.admin.add_link(MenuLink(name='Ir a plataforma', url='/', category='Administrador'))
        self.admin.add_link(MenuLink(name='Cerrar Sesion', url='/logout', category='Administrador'))

        self.path = op.join(op.dirname(__file__), 'static')
        self.admin.add_view(FileAdmin(self.path, '/static/', name='Static Files', category='Administrador'))
        
        """
        #    User Space
        """
        
        self.admin.add_view(
            UserAdmin(
                User, 
                name='Usuarios', 
                endpoint='admin_user',
                category='Usuarios'
            )
        )
        
        self.admin.add_view(
            RoleAdmin(
                Role, 
                name='Roles', 
                endpoint='admin_role',
                category='Usuarios'
            )
        )
        
        self.admin.add_view(
            UserRoleAdmin(
                UserRoles, 
                name='Vinculos', 
                endpoint='admin_user_role',
                category='Usuarios'
            )
        )