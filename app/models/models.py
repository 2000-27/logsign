from werkzeug.security import generate_password_hash, check_password_hash

from app import db, ma

class ManagementAccount(db.Model):
      
      id = db.Column(db.Integer,autoincrement=True, primary_key=True)
      username = db.Column(db.String(200))
      userpassword = db.Column(db.String(),unique=True)
      email = db.Column(db.String(100),unique=True)
      
      def __init__(self,username, userpassword,email ):
            self.username = username
            self.userpassword =userpassword
            self.email=email
            
      def set_password(self,userpassword):
        self.userpassword = generate_password_hash(userpassword)
        

      def check_password(self,userpassword):
        return check_password_hash(self.userpassword,userpassword)     

class signupSchema(ma.Schema):
      class Meta:
            fields=('id','username','userpassword','email')

single_data = signupSchema()
multiple_data = signupSchema(many=True)
