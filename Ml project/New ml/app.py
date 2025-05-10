from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("model.pkl")

class ShipmentData(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: int
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: int
    Weight_in_gms: int

@app.post("/predict")
def predict(data: ShipmentData):
    df = pd.DataFrame([data.dict()])

    # Encode categorical
    label_maps = {
        'Warehouse_block': {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4},
        'Mode_of_Shipment': {'Flight': 0, 'Ship': 1, 'Road': 2},
        'Product_importance': {'low': 1, 'medium': 2, 'high': 0},
        'Gender': {'M': 1, 'F': 0}
    }

    for col, mapping in label_maps.items():
        df[col] = df[col].map(mapping)

    prediction = model.predict(df)[0]
    return {"prediction": "On Time" if prediction == 1 else "Delayed"}
