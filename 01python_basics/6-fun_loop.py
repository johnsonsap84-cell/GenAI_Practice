#fuction to calculate the total price of products in the list
def print_my_list(products):
    for product in products:
        print(f"Name: {product['name']}, Price: {product['price']:.2f}, Quantity: {product['quantity']}, Category: {product['category']}")

def calculate_total_price(product):
    if product['category'] == "Fruits":
        product['price'] = product['price'] * product['quantity'] * 0.9  # 10% discount for fruits
    elif product['category'] == "Vegetables":
        product['price'] = product['price'] * product['quantity'] * 0.5  # 15% discount for vegetables
    elif product['category'] == "Dairy":
        product['price'] = product['price'] * product['quantity'] * 0.7  # 20% discount for dairy
    return product

#create a list of dictionary fruits Aand vegetables with name, price, quantity, and category
products = [
    {"name": "Apple", "price": 1.99, "quantity": 50, "category": "Fruits"},
    {"name": "Banana", "price": 0.99, "quantity": 30, "category": "Fruits"},
    {"name": "Carrot", "price": 2.49, "quantity": 20, "category": "Vegetables"},
    {"name": "Broccoli", "price": 1.49, "quantity": 15, "category": "Vegetables"},
    {"name": "Orange", "price": 1.29, "quantity": 40, "category": "Fruits"},
    {"name": "Spinach", "price": 1.99, "quantity":  25, "category": "Vegetables"},
    {"name": "Milk", "price": 2.99, "quantity": 10, "category": "Dairy"},
    {"name": "Cheese", "price": 3.99, "quantity": 5, "category": "Dairy"},
    {"name": "Yogurt", "price": 1.49, "quantity": 8, "category": "Dairy"},
]

#print("Products List:")
print_my_list(products)
print(calculate_total_price(products[0]))



    