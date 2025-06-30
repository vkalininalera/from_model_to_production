from flask import Flask, request, jsonify
import pickle

# Load the model
model = pickle.load(open('anomaly_model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [[
        data['temperature'],
        data['inertial_humidity'],
        data['sound']
    ]]
    prediction = model.predict(features).tolist()
    return jsonify({
        "prediction": prediction[0],
        "note": "0 = no anomaly detected, 1 = anomaly detected"
    })


if __name__ == '__main__':
    app.run(debug=True)
