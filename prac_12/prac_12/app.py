from flask import Flask
from flasgger import Swagger
from prac_12.config import DBConn

def create_app():
    app = Flask(__name__)
    Swagger(app)

    DBConn()

    @app.route('/')
    def hello():
        """
        Вернуть "hello"
        ---
        responses:
          200:
            description: ОК
        """
        return 'hello'

    from prac_12.blueprints import shelf
    app.register_blueprint(shelf, url_prefix='/shelf')

    return app
