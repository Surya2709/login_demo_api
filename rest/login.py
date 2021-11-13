"""
    This module used for access API endpoints
"""
from datetime import datetime
from flask import request, Blueprint, Response
from conf.database import Config
from controller.login import check_registration

USER_BLUEPRINT = Blueprint('user', __name__, url_prefix='/api/v1/')



@USER_BLUEPRINT.route('/resgistration', methods=["POST"])
def create_user_authenticate_api():
    body  = request.body
    resp =  check_registration(body)
    return resp

