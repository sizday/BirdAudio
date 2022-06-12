from flask import Flask
from config import Config
from blueprints import blueprint as basic_endpoints

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(basic_endpoints)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
