# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

class Shipment(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: float
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: float
    Weight_in_gms: float

@app.post("/predict")
def predict(data: Shipment):
    input_dict = data.dict()
    
    # Manual Encoding
    input_dict['Warehouse_block'] = encoders['Warehouse_block'].transform([input_dict['Warehouse_block']])[0]
    input_dict['Mode_of_Shipment'] = encoders['Mode_of_Shipment'].transform([input_dict['Mode_of_Shipment']])[0]
    input_dict['Product_importance'] = encoders['Product_importance'].transform([input_dict['Product_importance']])[0]
    input_dict['Gender'] = encoders['Gender'].transform([input_dict['Gender']])[0]

    features = list(input_dict.values())
    prediction = model.predict([features])[0]

    return {"prediction": int(prediction)}
