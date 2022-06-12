from flask import jsonify, request, make_response
from flask_restx import Namespace, Resource, fields


namespace = Namespace('predict', 'Predict endpoints')


@namespace.route('')
class Predict(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Predict')
    def post(self):
        audio_file = request.files['bird']
        audio_file.save('/')
        return None
