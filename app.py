from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    prediction = model.predict(vectorizer.transform([text]))[0]
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run()
