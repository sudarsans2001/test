from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_endpoint():
    sample_data = {
        "Warehouse_block": "F",
        "Mode_of_Shipment": "Flight",
        "Customer_care_calls": 3,
        "Customer_rating": 4,
        "Cost_of_the_Product": 100,
        "Prior_purchases": 2,
        "Product_importance": "low",
        "Gender": "M",
        "Discount_offered": 10,
        "Weight_in_gms": 500
    }

    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in [0, 1]
