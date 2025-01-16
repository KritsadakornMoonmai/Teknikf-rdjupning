from flask import Blueprint, jsonify

hello_route = Blueprint('Greetings', __name__)

@hello_route.route('/', methods=['GET'])
def Greetings():
    return jsonify('Hello!')