import numpy as np

# Create a random numpy array of shape (5, 6) with integers between 1 and 100
random_array = np.random.randint(1, 101, size=(5, 6))

print("Random Array:")
print(random_array)

# Compute the maximum integer for each row
max_per_row = np.max(random_array, axis=1)

print("\nMaximum Integer for Each Row:")
print(max_per_row)
