from app import le_warehouse, le_shipment, le_importance, le_gender

def test_label_encoders():
    assert le_warehouse.transform(["A"])[0] in range(5)
    assert le_shipment.transform(["Ship"])[0] in range(3)
    assert le_importance.transform(["low"])[0] in range(3)
    assert le_gender.transform(["F"])[0] in [0, 1]
