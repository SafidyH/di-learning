def is_mono(arr):
    is_increasing = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    is_decreasing = all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
    return is_increasing or is_decreasing

# Test the function
arr1 = [7, 6, 5, 5, 2, 0]
arr2 = [2, 3, 3, 3]
arr3 = [1, 2, 0, 4]

print(is_mono(arr1))
print(is_mono(arr2))
print(is_mono(arr3))
