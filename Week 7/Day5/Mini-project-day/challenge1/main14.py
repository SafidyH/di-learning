def dict_avg(dictionary):
    values = list(dictionary.values())
    average = sum(values) / len(values)
    return average

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 8, 'd': 1}
result = dict_avg(my_dict)
print(result)  # 3.0
