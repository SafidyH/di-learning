basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")  # Remove "Banana" from the list
basket.remove("Blueberries")  # Remove "Blueberries" from the list

basket.append("Kiwi")  # Add "Kiwi" to the end of the list
basket.insert(0, "Apples")  # Add "Apples" to the beginning of the list

apple_count = basket.count("Apples")  # Count how many "Apples" are in the basket

basket.clear()  # Empty the basket

print(basket)  # Print the contents of the basket (should be an empty list)
