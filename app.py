
from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    prediction = model.predict(vectorizer.transform([text]))[0]
    confidence = max(model.predict_proba(vectorizer.transform([text]))[0])
    return render_template('result.html', 
                         text=text,
                         prediction=prediction,
                         confidence=round(confidence*100, 2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
