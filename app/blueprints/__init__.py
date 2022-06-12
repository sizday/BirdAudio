from flask import Blueprint
from flask_restx import Api
from blueprints.predict import namespace as predict_ns

async_mode = None
thread = None
blueprint = Blueprint('api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='BirdAudio REST',
    version='1.0',
    description='API BoardFriends',
    doc='/doc'
)

api_extension.add_namespace(predict_ns)
