from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

from src.controllers.nse import Nse

api.add_resource(Nse, '/nse')
