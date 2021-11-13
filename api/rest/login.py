"""
    This module used for access API endpoints
"""
from flask import request, Blueprint
from api.controller.login import check_registration
from api.controller.login import login


USER_BLUEPRINT = Blueprint('user', __name__, url_prefix='/api/v1/')



@USER_BLUEPRINT.route('/resgistration', methods=["POST"])
def create_user_authenticate_api():
    body  = request.json
    resp =  check_registration(body)
    return resp

@USER_BLUEPRINT.route('/login',methods = ['POST'])
def check_login():

    body = request.json
    resp = login(body)

    return resp