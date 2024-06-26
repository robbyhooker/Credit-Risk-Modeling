from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('credit_rf_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    input_data = pd.DataFrame(data, index=[0])

    # Make predictions
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)[:, 1]

    return jsonify({
        'prediction': int(prediction[0]),
        'probability': prediction_proba[0]
    })

if __name__ == '__main__':
    app.run(debug=True)
