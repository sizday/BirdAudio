from flask import jsonify, request, make_response, send_file
from flask_restx import Namespace, Resource, fields
import os

namespace = Namespace('birds', 'Info endpoints')


@namespace.route('/info')
class BirdsInfo(Resource):
    @namespace.response(404, 'Birds info not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Get info about all birds')
    def get(self):
        dirname = 'data/txt/'
        birds_info = []
        for filename in os.listdir(dirname):
            with open(os.path.join(dirname, filename), 'r', encoding='utf-8') as file:
                bird_info = file.read()
                bird_rus_name, bird_description = bird_info.split('\n')
                info_dict = {'name': bird_rus_name, 'description': bird_description}
                birds_info.append(info_dict)
        return jsonify(birds_info)


@namespace.route('/info/<bird_name>')
class BirdInfo(Resource):
    @namespace.response(404, 'Bird info not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Get bird info by name')
    def get(self, bird_name):
        filename = f'data/txt/{bird_name}.txt'
        with open(filename, 'r', encoding='utf-8') as file:
            bird_info = file.read()
            bird_rus_name, bird_description = bird_info.split('\n')
        info_dict = {'name': bird_rus_name, 'description': bird_description}
        return jsonify(info_dict)


@namespace.route('/img/<bird_name>')
class BirdImg(Resource):
    @namespace.response(404, 'Bird img not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.doc('Get bird img by name')
    def get(self, bird_name):
        ext = 'jpg'
        filename = f'data/img/{bird_name}.{ext}'
        return send_file(filename, mimetype=f'image/{ext}')
