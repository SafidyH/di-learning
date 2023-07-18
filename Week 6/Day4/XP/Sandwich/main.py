sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []
removed_count = 0

# Removing all occurrences of "Pastrami sandwich" from sandwich_orders
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    removed_count += 1

print(f"Removed {removed_count} occurrences of 'Pastrami sandwich' from sandwich_orders.")

# Preparing the orders
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")

print("\nList of sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
