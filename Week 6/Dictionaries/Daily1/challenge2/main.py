items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

# Remove the dollar sign and convert the wallet amount to an integer
wallet_amount = int(wallet.replace("$", ""))

affordable_items = []  # Initialize an empty list to store affordable items

# Iterate over each item in the items_purchase dictionary
for item, price in items_purchase.items():
    # Remove the dollar sign and convert the item price to an integer
    item_price = int(price.replace("$", "").replace(",", ""))

    # Check if the wallet amount is greater than or equal to the item price
    if wallet_amount >= item_price:
        affordable_items.append(item)  # Add the item to the list of affordable items

# Sort the affordable_items list in alphabetical order
affordable_items.sort()

# Print the resulting list of affordable items or "Nothing" if the list is empty
if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
