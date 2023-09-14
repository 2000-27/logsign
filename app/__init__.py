from flask import Flask,Blueprint

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from app.configs import DevConfig
from .routes import new_mold
app = Flask(__name__)


app.config.from_object(DevConfig)

app.register_blueprint(new_mold, url_prefix='/api')

db = SQLAlchemy()
ma = Marshmallow()

from app.models import (
    ManagementAccount
)
db.init_app(app)

with app.app_context():
    db.create_all()
    
