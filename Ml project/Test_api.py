import sys
import os

# Add the root directory (where app.py is) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # imports app instance from app.py

from fastapi.testclient import TestClient

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={
        "Warehouse_block": "F",
        "Mode_of_Shipment": "Flight",
        "Customer_care_calls": 3,
        "Customer_rating": 4,
        "Cost_of_the_Product": 250,
        "Prior_purchases": 2,
        "Product_importance": "high",
        "Gender": "F",
        "Discount_offered": 20,
        "Weight_in_gms": 2000
    })
    assert response.status_code == 200
    assert "prediction" in response.json()
