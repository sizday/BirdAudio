from flask import jsonify, request, make_response
from flask_restx import Namespace, Resource, fields


namespace = Namespace('fit', 'Fit endpoints')


@namespace.route('')
class Predict(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Fit')
    def post(self):
        pass
