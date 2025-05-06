import joblib
import os
import numpy as np

def test_model_load():
    assert os.path.exists("model.pkl"), "Model file not found."
    model = joblib.load("model.pkl")
    assert model is not None

def test_model_prediction():
    model = joblib.load("model.pkl")
    sample_input = [[3, 3, 4, 100, 2, 1, 0, 1, 10, 500]]  # Replace with your input format
    prediction = model.predict(sample_input)
    assert prediction[0] in [0, 1], "Prediction should be binary"
