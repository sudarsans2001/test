from fastapi import FastAPI
from schemas import ShipmentFeatures
import joblib
import numpy as np

app = FastAPI()

# Load the model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Shipment Delay Prediction API is live."}

@app.post("/predict")
def predict(data: ShipmentFeatures):
    input_data = np.array([[ 
        data.Warehouse_block,
        data.Mode_of_Shipment,
        data.Customer_care_calls,
        data.Customer_rating,
        data.Cost_of_the_Product,
        data.Prior_purchases,
        data.Product_importance,
        data.Gender,
        data.Discount_offered,
        data.Weight_in_gms
    ]])

    prediction = model.predict(input_data)
    result = "On Time" if prediction[0] == 1 else "Delayed"
    return {"prediction": result}
