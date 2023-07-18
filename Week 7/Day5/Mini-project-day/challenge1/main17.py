def weird_print(lst):
    result = []
    for index, value in enumerate(lst):
        if index % 2 == 0 and value % 2 == 0:
            result.append(value)
    return result

# Example usage
result = weird_print([1, 2, 2, 3, 4, 5])
print(result)  # [2, 4]
