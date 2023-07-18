items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("Items and their prices:")
for item, price in items.items():
    print(f"{item}: ${price}")

items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0
for item, data in items.items():
    price = data["price"]
    stock = data["stock"]
    total_cost += price * stock

print(f"The total cost to buy everything in stock is: ${total_cost}")
