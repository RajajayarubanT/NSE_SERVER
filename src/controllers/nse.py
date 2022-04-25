from src.services.service import findresult
from flask import request, jsonify, make_response, request
from flask_restful import Resource, Api, abort, reqparse

parser = reqparse.RequestParser()
parser.add_argument('symbol', action='append')
parser.add_argument('query', action='append')
parser.add_argument('start', action='append')
parser.add_argument('end', action='append')
parser.add_argument('expiry', action='append')

class Nse(Resource):
    def post(self):
        response = {}
        data = {}
        args = parser.parse_args()
        print(args)
        result = findresult(args.symbol[0], args.query[0], args.start[0], args.end[0], args.expiry)
        print(result)
        if result :
            response['message'] = "success"
            data['result'] = result
            response['data']= data
            return response, 200
        else :
            response['message'] = "Invalid inputs"
            return response, 400


    
    