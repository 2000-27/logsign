import os
from dotenv import load_dotenv

load_dotenv()


class DevConfig(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    email = "test@gmail.com"
    SECRET_KEY = os.environ['SECRET_KEY']

    google_api_key = os.environ.get('google_api_key')
    
   


# class ProductionConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'
#     Paytm = 'pqr'


# class DevelopmentConfig(Config):
#     DATABASE_URI = "sqlite:////tmp/foo.db"
#     Paytm = 'xyz'


# class TestingConfig(Config):
#     DATABASE_URI = 'sqlite:///:memory:'
#     TESTING = True