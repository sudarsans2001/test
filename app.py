from fastapi import FastAPI
from schemas import ShipmentFeatures
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = FastAPI()

# Load the model
model = joblib.load("model.pkl")

# Initialize LabelEncoders with the same mappings as Model.py
le_warehouse = LabelEncoder()
le_warehouse.classes_ = np.array(['A', 'B', 'C', 'D', 'F'])

le_shipment = LabelEncoder()
le_shipment.classes_ = np.array(['Flight', 'Ship', 'Road'])

le_importance = LabelEncoder()
le_importance.classes_ = np.array(['low', 'medium', 'high'])

le_gender = LabelEncoder()
le_gender.classes_ = np.array(['F', 'M'])

@app.get("/")
def home():
    return {"message": "Shipment Delay Prediction API is live."}

@app.post("/predict")
def predict(data: ShipmentFeatures):
    # Encode categorical features
    warehouse_encoded = le_warehouse.transform([data.Warehouse_block])[0]
    shipment_encoded = le_shipment.transform([data.Mode_of_Shipment])[0]
    importance_encoded = le_importance.transform([data.Product_importance])[0]
    gender_encoded = le_gender.transform([data.Gender])[0]

    # Prepare input data for model
    input_data = np.array([[
        warehouse_encoded,
        shipment_encoded,
        data.Customer_care_calls,
        data.Customer_rating,
        data.Cost_of_the_Product,
        data.Prior_purchases,
        importance_encoded,
        gender_encoded,
        data.Discount_offered,
        data.Weight_in_gms
    ]])

    prediction = model.predict(input_data)
    result = "On Time" if prediction[0] == 1 else "Delayed"
    return {"prediction": result}