from werkzeug.security import generate_password_hash

from app import db

class ManagementAccount(db.Model):
      id = db.Column(db.Integer,autoincrement=True, primary_key=True)
      username = db.Column(db.String())
      userpassword = db.Column(db.String(),unique=True)
      email = db.Column(db.String(),unique=True)
      def __init__(self,username, userpassword,email ):
            self.username = username
            self.userpassword =userpassword
            self.email=email
      def set_password(self,userpassword):
        self.password_hash = generate_password_hash(userpassword)


