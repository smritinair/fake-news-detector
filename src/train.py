# Add this at the top
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("data/news_sample.csv")
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])
model = LogisticRegression().fit(X, df['label'])
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
# Add this after model training
print(classification_report(y_test, model.predict(X_test)))
