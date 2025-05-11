import pytest
from fastapi.testclient import TestClient
from app import app
from schemas import ShipmentFeatures

client = TestClient(app)

# Sample input for testing
valid_payload = {
    "Warehouse_block": "A",
    "Mode_of_Shipment": "Flight",
    "Customer_care_calls": 4,
    "Customer_rating": 3,
    "Cost_of_the_Product": 250.0,
    "Prior_purchases": 2,
    "Product_importance": "medium",
    "Gender": "M",
    "Discount_offered": 5.0,
    "Weight_in_gms": 1500.0
}

invalid_payload = {
    "Warehouse_block": "Z",  # Invalid category
    "Mode_of_Shipment": "Bike",  # Invalid category
    "Customer_care_calls": -1,  # Invalid value
    "Customer_rating": 10,  # Out of valid range
    "Cost_of_the_Product": -50.0,
    "Prior_purchases": 100,
    "Product_importance": "extreme",
    "Gender": "X",
    "Discount_offered": 105.0,
    "Weight_in_gms": -999.0
}

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Shipment Delay Prediction API is live."}

def test_predict_valid():
    response = client.post("/predict", json=valid_payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in ["On Time", "Delayed"]

def test_predict_invalid():
    response = client.post("/predict", json=invalid_payload)
    # Expecting validation or processing error
    assert response.status_code in [400, 422]
