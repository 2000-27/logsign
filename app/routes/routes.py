from flask import request,jsonify, Blueprint, current_app
# from app import db,app,new_mold

from datetime import datetime,timedelta
import jwt
 
import re


new_mold=Blueprint("auth",__name__)

@new_mold.route('/register', methods =['POST'])
def register():
  from app import db
  from app.models import ManagementAccount, single_data
  try:  
    json_body = request.get_json()
    msg = ''
    if request.method == 'POST'  :
        username = json_body['username']
        userpassword = json_body['userpassword']
        email = json_body['email']
                  
        if not re.match(r'[^@]+@[^@]+\.[^@]+',email):
           msg = 'Invalid email address !'
         
        elif not (re.match(r'[a-zA-Z0-9\s]+$', username)):
           msg = 'Username must contain only characters  and space !!!!!'
        
        else:
                 msg = 'REGISTER SUCCESSFULLY!'
                 new_product = ManagementAccount(username, userpassword, email)
                 new_product.set_password(userpassword)
                 db.session.add(new_product)
                 db.session.commit()
                 return single_data.jsonify(new_product)
        return jsonify(username,userpassword,email,msg)
  except :
    msg="ALREADY RECORD IS EXIT "
    return jsonify({"msg": msg})


def checkpass(email):
  from app import db
  from app.models import ManagementAccount, single_data
  all_product=ManagementAccount.query.filter_by(email=email).first()

  print("ALL PRODUCT: ",all_product)
  result = single_data.dump(all_product)
  print("your emai id is correct and result is => ",result)
  return result


@new_mold.route('/login', methods =['POST'])
def login():
    json_body = request.get_json()
    from app import app 
    msg = ''
    if request.method == 'POST':
        userpassword = json_body['userpassword']
        email = json_body['email']
        print("password and email id iss => ",userpassword,email)
    
        try:  
           result=checkpass(email)
           if result=={}:
               msg="PLEASE LOGIN !!!"
               print(msg)
           else:    
               msg="SIGN UP SUCCESSFULLY !!!!"
               print(msg)  
               token = jwt.encode({'public_id': 1,'exp' :str( datetime.utcnow() + timedelta(minutes = 30)) }, app.config['SECRET_KEY'])
               print("your token is  =>>>>",token)
               return jsonify(message="Login Succeeded!", access_token=token)
               
 
        except  Exception as error:
          msg= 'there is no user '
          print("your exception is ",error) 
            


        return jsonify({"msg": msg})

