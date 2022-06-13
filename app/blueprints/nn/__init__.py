import os.path

from flask import jsonify, request, make_response
from flask_restx import Namespace, Resource, fields
from utils.create_spectrogram import get_sample
from utils.predict import create_result, get_argmax_elem_name
from werkzeug.utils import secure_filename

namespace = Namespace('nn', 'Neural network endpoints')


@namespace.route('/predict')
class Predict(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Predict')
    def post(self):
        dirname = 'data/records/'
        audio_file = request.files['audio']
        filename = secure_filename(audio_file.filename)
        name, ext = os.path.splitext(filename)
        filename_mp3 = os.path.join(dirname, filename)
        filename_tif = os.path.join(dirname, f"{name}.tif")
        audio_file.save(filename_mp3)

        get_sample(filename_mp3, name, dirname)
        tensor = create_result(filename_tif)
        result = get_argmax_elem_name(tensor)
        os.remove(filename_mp3)
        os.remove(filename_tif)

        return result


@namespace.route('/fit')
class Fit(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Fit')
    def post(self):
        pass
