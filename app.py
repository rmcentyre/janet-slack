import os

import dotenv
from flask import Flask, Blueprint
from flask_restful import Api

from resources import GoodJanet, BadJanet

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(GoodJanet, '/bot/janet')
api.add_resource(BadJanet, '/bot/badjanet')

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run()
