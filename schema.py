from pydantic import BaseModel

class ShipmentFeatures(BaseModel):
    Warehouse_block: str  # e.g., A, B, C, D, F
    Mode_of_Shipment: str  # e.g., Flight, Ship, Road
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: float
    Prior_purchases: int
    Product_importance: str  # e.g., low, medium, high
    Gender: str  # e.g., F, M
    Discount_offered: float
    Weight_in_gms: float