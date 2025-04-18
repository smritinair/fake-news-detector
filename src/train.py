# Add this at the top
from sklearn.metrics import classification_report

# Add this after model training
print(classification_report(y_test, model.predict(X_test)))
