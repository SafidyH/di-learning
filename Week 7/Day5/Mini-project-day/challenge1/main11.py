def separate_integers_and_strings(lst):
    integers = []
    strings = []

    for item in lst:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)

    return integers, strings

# Example usage
mixed_list = [10, 'apple', 20, 'banana', 'cherry', 30, 'durian']
integers, strings = separate_integers_and_strings(mixed_list)

print("Integers:", integers)
print("Strings:", strings)
