from flask import Blueprint
from flask_restful import Resource, Api, abort
from functools import wraps
from flask_httpauth import HTTPBasicAuth
from clux.models.user import User

auth = HTTPBasicAuth()
api_bp = Blueprint('api', __name__)

api = Api(api_bp)

@auth.verify_password
def verify_password(username, password):
    print(username, password)
    return False

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        # acct = basic_authentication()  # custom account lookup function
        acct = False  # custom account lookup function

        if acct:
            return func(*args, **kwargs)

        abort(401)
    return wrapper


class Resource(Resource):
    # method_decorators = [authenticate]
    method_decorators = [auth.login_required]

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')
