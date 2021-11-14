"""
    This module used for access API endpoints
"""
from flask import request, Blueprint, Response as response
from api.controller.login import registration
from api.controller.login import login
import json
from utils.helper import validate_body


USER_BLUEPRINT = Blueprint('user', __name__, url_prefix='/api/v1/')



@USER_BLUEPRINT.route('/resgistration', methods=["POST"])
def regeister():
    
    body  = request.json
    if not validate_body(body):
        return response(status= 400, response=json.dumps( {"resp": "Invalid  req obj"}))

    resp =  registration(body)
    return response(status= resp[0], response=json.dumps(resp[1]))

@USER_BLUEPRINT.route('/login',methods = ['POST'])
def check_login():

    body = request.json
    resp = login(body)

    return response(status= resp[0], response=json.dumps(resp[1]))
