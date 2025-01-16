from flask import Blueprint, jsonify, request
from Events.fetch_data import FetchModel
from Events.Preprocess_data import PreprocessData
import joblib

spam_result_route = Blueprint('SpamResult', __name__, url_prefix='/api')
fetch_model = FetchModel()
fetched_model = fetch_model.fetch()

@spam_result_route.route('/predict', methods=['POST'])
def predict():
    try:
        get_req = request.get_json()
        print('Request: ')
        print(get_req)
        if 'email' not in get_req:
                return jsonify({"error": "Email is required"}), 400
        input_text = get_req['email']
        input_vector = fetched_model[1].transform([input_text])
        prediction = fetched_model[0].predict_proba(input_vector)[0][1]
        print('spam prob result: ')
        print(prediction * 100)
        return jsonify({"spam_prob": prediction * 100})
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500