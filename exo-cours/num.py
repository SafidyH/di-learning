my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        try:
            total += int(num)
        except TypeError:
            pass
    return total


result = calculate_sum(my_list)
print(result)