def concatenate_lists(list1, list2):
    concatenated = []
    for item in list1:
        concatenated.append(item)
    for item in list2:
        concatenated.append(item)
    return concatenated

# Example usage
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = concatenate_lists(list1, list2)
print(result)
