reviews = [
    {"product": "Laptop", "rating": 4.5},
    {"product": "Phone", "rating": 4.0},
    {"product": "Laptop", "rating": 3.5},
    {"product": "Tablet", "rating": 5.0},
    {"product": "Phone", "rating": 3.8},
    {"product": "Laptop", "rating": 4.2}
]

product_ratings = {}


for review in reviews:
    product = review["product"]
    rating = review["rating"]
    
    if product not in product_ratings:
        product_ratings[product] = [0, 0]  
    
    product_ratings[product][0] += rating  
    product_ratings[product][1] += 1  


average_ratings = {}
for product, data in product_ratings.items():
    average_ratings[product] = round(data[0] / data[1], 2)

print(average_ratings)
