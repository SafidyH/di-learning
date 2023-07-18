def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test the function
numbers = [0, 1, 3, 50]
result = find_max(numbers)
print(result)
