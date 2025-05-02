from pydantic import BaseModel

class ShipmentFeatures(BaseModel):
    Warehouse_block: int
    Mode_of_Shipment: int
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: int
    Prior_purchases: int
    Product_importance: int
    Gender: int
    Discount_offered: int
    Weight_in_gms: int
