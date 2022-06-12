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
        filename_mp3 = 'data/records/crow.mp3'
        filename_tif = 'data/records/crow.tif'
        dirname = 'data/records/'
        get_sample(filename_mp3, 'crow', dirname)
        tensor = create_result(filename_tif)
        result = get_argmax_elem_name(tensor)

        return result


@namespace.route('/fit')
class Fit(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Fit')
    def post(self):
        pass
