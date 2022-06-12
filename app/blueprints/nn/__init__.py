from flask import jsonify, request, make_response
from flask_restx import Namespace, Resource, fields


namespace = Namespace('nn', 'Neural network endpoints')


@namespace.route('/predict')
class Predict(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Predict')
    def post(self):
        audio_file = request.files['bird']
        audio_file.save('/')
        return None


@namespace.route('/fit')
class Fit(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Fit')
    def post(self):
        pass
