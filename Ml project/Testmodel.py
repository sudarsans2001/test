# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("train.csv")

# Drop non-feature columns
df.drop(columns=["ID"], inplace=True, errors="ignore")

# Encode categorical variables
df = pd.get_dummies(df, columns=["Warehouse_block", "Mode_of_Shipment", "Product_importance", "Gender"], drop_first=True)

# Separate features and target
X = df.drop(columns=["Reached_on_Time_Y_N"])
y = df["Reached_on_Time_Y_N"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and feature columns
joblib.dump(model, "model.pkl")
joblib.dump(X.columns.tolist(), "features.pkl")

print("Model and feature columns saved.")
