from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Routes import hello
from Routes import messages
from Routes import spam_result
def create_app():

    app = Flask(__name__)

    CORS(app, resources={r'/*': {'origins': '*'}})

    api = Api(app)

    app.register_blueprint(hello.hello_route)
    app.register_blueprint(messages.messages_route)
    app.register_blueprint(spam_result.spam_result_route)

    return app