import joblib
import numpy as np

def test_model_loading():
    model = joblib.load("model.pkl")
    assert model is not None

def test_model_prediction_shape():
    model = joblib.load("model.pkl")
    sample_input = np.array([[1, 0, 3, 4, 200.0, 2, 1, 1, 10.0, 1000.0]])
    pred = model.predict(sample_input)
    assert len(pred) == 1
    assert pred[0] in [0, 1]
