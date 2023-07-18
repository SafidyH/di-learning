toppings = []
total_price = 10

while True:
    topping = input("Enter a topping (or 'quit' to exit): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    total_price += 2.5
    print("Adding", topping, "to your pizza.")

print("Toppings on your pizza:", ", ".join(toppings))
print("Total price:", total_price)
