import numpy as np

def analyze_array(arr):
    min_value = np.min(arr)
    std_deviation = np.std(arr)
    product = np.prod(arr)
    dot_product = np.dot(arr, arr)
    subtracted_array = arr - 4
    return min_value, std_deviation, product, dot_product, subtracted_array

# Example usage
input_array = np.array([1, 2, 3, 4, 5])
result = analyze_array(input_array)
print(result)
