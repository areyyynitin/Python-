info = {"name": "Nitin", "age": 21, "city": "Mumbai"}

print("Key:", info.keys())  
print("Value:", info.values())  
print("Item:", info.items())  
print("Age:", info.get("age"))  

info["country"] = "India"  
print("Updated:", info)  

info.pop("city")  
print("After Removal:", info)  

print("State:", info.get("state", "Not Available"))  
