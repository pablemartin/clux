from clux.models.user import User, Role, UserRoles
from clux.db import db

from flask_security import (
    Security,
    PeeweeUserDatastore,
    UserMixin,
    RoleMixin,
    login_required
)

class AuthManager():
    """ Manager of security

    Include
    - Registration without email confirmation
    - Login
    - Forgot password
    - Change Password
    """
    def __init__(self, app):
        # Setup Flask-Security
        self.user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
        self.security = Security(app, self.user_datastore, register_blueprint=True)
