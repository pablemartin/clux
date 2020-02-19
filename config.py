import os
from dotenv import load_dotenv
load_dotenv()

class ConfigBase(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'UnaClaveSecretaParaBioleft'
    SECURITY_PASSWORD_SALT = 'super-secret-random-salt'
    DATABASE={
        'name': os.environ.get("POSTGRES_NAME"),
        'user': os.environ.get("POSTGRES_USER"),
        'host': os.environ.get("POSTGRES_HOST"),
        'port': os.environ.get("POSTGRES_PORT"),
        'password': os.environ.get("POSTGRES_PASSWORD")
    }

    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    SECURITY_REGISTERABLE = os.environ.get('SECURITY_REGISTERABLE')
    SECURITY_RECOVERABLE = os.environ.get('SECURITY_RECOVERABLE')
    SECURITY_CHANGEABLE = os.environ.get('SECURITY_CHANGEABLE')
    SECURITY_SEND_REGISTER_EMAIL = os.environ.get('SECURITY_SEND_REGISTER_EMAIL')
    SECURITY_CONFIRMABLE = os.environ.get('SECURITY_CONFIRMABLE')
    SECURITY_TRACKABLE = os.environ.get('SECURITY_TRACKABLE')
    SECURITY_URL_PREFIX = os.environ.get('SECURITY_URL_PREFIX')
    SECURITY_POST_CONFIRM_VIEW = os.environ.get('SECURITY_POST_CONFIRM_VIEW')
    SECURITY_CONFIRM_ERROR_VIEW = os.environ.get('SECURITY_CONFIRM_ERROR_VIEW')
    SECURITY_REET_VIEW = os.environ.get('SECURITY_REET_VIEW')
    SECURITY_RESET_ERROR_VIEW = os.environ.get('SECURITY_RESET_ERROR_VIEW')
    SECURITY_REDIRECT_BEHAVIOR = os.environ.get('SECURITY_REDIRECT_BEHAVIOR')
    SECURITY_PASSWORDLESS = os.environ.get('SECURITY_PASSWORDLESS')
    SECURITY_TWO_FACTOR = os.environ.get('SECURITY_TWO_FACTOR')

class DevelopmentConfig(ConfigBase):
    ENV='development'
    DEBUG=True

class ProductionConfig(ConfigBase):
    ENV='production'
    DEBUG=False

Config = DevelopmentConfig