
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("train.csv")  # Ensure this file is downloaded from Kaggle

# Drop duplicates and check for nulls
df = df.drop_duplicates()
df = df.dropna()

# Encode categorical features
le = LabelEncoder()
df['Warehouse_block'] = le.fit_transform(df['Warehouse_block'])
df['Mode_of_Shipment'] = le.fit_transform(df['Mode_of_Shipment'])
df['Product_importance'] = le.fit_transform(df['Product_importance'])
df['Gender'] = le.fit_transform(df['Gender'])

# Define features and target
X = df.drop(columns=['ID', 'Reached.on.Time_Y.N'])  # Drop ID and target
y = df['Reached.on.Time_Y.N']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
