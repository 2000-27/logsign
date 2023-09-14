from flask import request,jsonify, Blueprint, current_app
from datetime import datetime,timedelta
import jwt
import re
from app.models import ManagementAccount
from app.schema import signupSchema
from app import db


new_mold=Blueprint("auth",__name__)
single_data = signupSchema()
@new_mold.route('/register', methods =['POST'])
def register():
  try:  
    json_body = request.get_json()
    msg = ''
    if request.method == 'POST'  :
        username = json_body['username']
        userpassword = json_body['userpassword']
        email = json_body['email']
        if not re.match(r'[^@]+@[^@]+\.[^@]+',email):
           msg = 'INVALID EMAIL ADDRESS !!!!'
         
        elif not (re.match(r'[a-zA-Z0-9\s]+$', username)):
           msg = 'Username must contain only characters , digit  and space !!!!!'
        
        else:
                 msg = 'REGISTER SUCCESSFULLY!'
                 new_product = ManagementAccount(username, userpassword, email)
                 new_product.set_password(userpassword)
                 db.session.add(new_product)
                 db.session.commit()
                 return single_data.jsonify(new_product)
        return jsonify(username,userpassword,email,msg)
  except :
    msg="RECORD IS EXIT !!!!!!!!!!!!! "
    return jsonify({"msg": msg})



@new_mold.route('/login', methods =['POST'])
def login():
    json_body = request.get_json()
    
    msg = ''
    if request.method == 'POST':
        userpassword = json_body['userpassword']
        email = json_body['email']
        try:  
           check_email=ManagementAccount.query.filter_by(email=email).first()
           result = single_data.dump(check_email)
           if result=={}:
               msg="PLEASE SIGNUP  !!!"
               
           else:    
               msg="SIGN UP SUCCESSFULLY !!!!"
               token = jwt.encode({'public_id': 1,'exp' :str( datetime.utcnow() + timedelta(minutes = 30)) }, current_app.config.get('SECRET_KEY'))
               return jsonify(message="  LOGIN SUCCESSFULLY !!! ", access_token=token)
               
        except  Exception as error:
          msg= 'THERE IS NO USER !!!!'
        
        return jsonify({"msg": msg})

