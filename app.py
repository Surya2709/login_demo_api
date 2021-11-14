from conf.database import Config
from maker import create_app
from flask_cors import CORS
from utils.helper import validate_token


app = create_app()
CORS(app)

@app.before_request
def before_request():
    return validate_token()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT, debug=True)
