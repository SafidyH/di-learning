class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cats):
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

# Instantiate three Cat objects
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Fluffy", 8)
cat3 = Cat("Mittens", 3)

# Create a list of cats
cats = [cat1, cat2, cat3]

# Find the oldest cat
oldest_cat = find_oldest_cat(cats)

# Print the information about the oldest cat
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
