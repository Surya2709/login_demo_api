from conf.database import Config
from flask import request,Response as response
from errors import ERRORS
import json

def validate_token():
    if not str(Config.TOKEN) == (request.headers.get('access_key')):
        return response(status=401,response= json.dumps(ERRORS['INVALID_TOKEN']))