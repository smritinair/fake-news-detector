import joblib
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict(text):
    return model.predict(vectorizer.transform([text]))[0]
📄 requirements.txt
