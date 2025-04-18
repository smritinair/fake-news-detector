import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("../data/news_sample.csv")
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
model = LogisticRegression().fit(X_train_vec, y_train)
joblib.dump(model, "../models/trained_model.pkl")
joblib.dump(vectorizer, "../models/vectorizer.pkl")
