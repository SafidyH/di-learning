import numpy as np

def calculate_difference(arr):
    max_values = np.max(arr, axis=1)
    min_values = np.min(arr, axis=1)
    differences = max_values - min_values
    return differences

# Example usage
input_array = np.array([[3, 8, 1],
                        [6, 2, 9],
                        [4, 7, 5]])

result = calculate_difference(input_array)
print(result)
