# tests/test_model.py
import joblib
import numpy as np

def test_model_prediction():
    model = joblib.load("model.pkl")
    sample = np.array([[4, 0, 3, 4, 250, 2, 2, 1, 20, 2000]])  # encoded sample
    prediction = model.predict(sample)
    assert prediction[0] in [0, 1]
