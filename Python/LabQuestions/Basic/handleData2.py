import json


with open("data.json", "r") as file:
    data = json.load(file)


required_fields = {
    "Product ID": int,
    "Name": str,
    "Price": float
}

def validate_json(data):
    for i, item in enumerate(data):
        for field, expected_type in required_fields.items():
            if field not in item:
                print("Error: Missing", field, "in item", i + 1)
            elif not isinstance(item[field], expected_type):
                print("Error:", field, "in item", i + 1, "should be", expected_type.__name__, "but found", type(item[field]).__name__)


validate_json(data)
