import os
from dotenv import load_dotenv

load_dotenv()


class DevConfig(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ['SECRET_KEY']

 
   

