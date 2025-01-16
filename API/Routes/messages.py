from flask import Blueprint, jsonify

messages_route = Blueprint('MessageInput', __name__, url_prefix='/api')

@messages_route.route('/message_input', methods=['GET'])
def MessageInput():
    return 