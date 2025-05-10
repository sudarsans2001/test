curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{
  "Warehouse_block": "F",
  "Mode_of_Shipment": "Flight",
  "Customer_care_calls": 4,
  "Customer_rating": 3,
  "Cost_of_the_Product": 200,
  "Prior_purchases": 2,
  "Product_importance": "low",
  "Gender": "M",
  "Discount_offered": 10,
  "Weight_in_gms": 2000
}'
