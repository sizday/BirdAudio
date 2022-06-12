from flask import Blueprint
from flask_restx import Api
from blueprints.info import namespace as info_ns
from blueprints.nn import namespace as nn_ns

async_mode = None
thread = None
blueprint = Blueprint('api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='BirdAudio REST',
    version='1.0',
    description='API BirdAudio',
    doc='/doc'
)

api_extension.add_namespace(info_ns)
api_extension.add_namespace(nn_ns)
