# Convert the string into a list
manufacturers = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(", ")

# Print the number of manufacturers/companies in the list
num_manufacturers = len(manufacturers)
print(f"There are {num_manufacturers} manufacturers/companies in the list.")

# Print the list of manufacturers in reverse order
print("Manufacturers in reverse order:")
print(", ".join(reversed(manufacturers)))

# Find the number of manufacturers' names with the letter 'o'
num_o = sum(1 for manufacturer in manufacturers if 'o' in manufacturer)
print(f"The number of manufacturers' names with the letter 'o' is: {num_o}")

# Find the number of manufacturers' names without the letter 'i'
num_no_i = sum(1 for manufacturer in manufacturers if 'i' not in manufacturer)
print(f"The number of manufacturers' names without the letter 'i' is: {num_no_i}")

# Remove duplicates from the list
manufacturers = list(set(manufacturers))

# Print the companies without duplicates
print("Companies without duplicates:")
print(", ".join(manufacturers))
num_unique = len(manufacturers)
print(f"There are {num_unique} companies in the list.")

# Print the list of manufacturers in ascending order with reversed names
print("Manufacturers in ascending order with reversed names:")
manufacturers_sorted = sorted(manufacturers, key=lambda x: x[::-1])
print(", ".join(manufacturers_sorted))
