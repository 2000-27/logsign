from app import ma 


class signupSchema(ma.Schema):
      class Meta:
            fields=('id','username','userpassword','email')


