from flask import jsonify, request, make_response
from flask_restx import Namespace, Resource, fields
from utils.create_spectrogram import get_sample
from utils.predict import create_result, get_argmax_elem_name

namespace = Namespace('nn', 'Neural network endpoints')


@namespace.route('/predict')
class Predict(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Predict')
    def get(self):
        # audio_file = request.files['bird']
        # audio_file.save('/')
        ext = ['mp3', 'tif']
        filename = 'data/record/crow.'
        get_sample(filename+ext[0], 'crow', 'data/record/')
        tensor = create_result(filename+ext[1])
        result = get_argmax_elem_name(tensor)

        return result


@namespace.route('/fit')
class Fit(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Fit')
    def post(self):
        pass
