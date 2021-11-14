import re
from conf.database import Config
from flask import request,Response as response
from errors import ERRORS
import json

def validate_token():
    if not str(Config.TOKEN) == (request.headers.get('access_key')):
        return response(status=401,response= json.dumps(ERRORS['INVALID_TOKEN']))


def validate_body(body):
    
    password = body.get("user_pass")
    flag = 0
    while True:  
        if (len(password)<8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            break
    
    if flag ==-1:
        return False
    
    if not body.get('user_name',None) or  not body.get("first_name",None) or not body.get("last_name",None) or not body.get("dob",None) :
        return False

    return True



