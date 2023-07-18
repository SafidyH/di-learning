def type_count(**kwargs):
    type_counts = {}
    for value in kwargs.values():
        value_type = type(value).__name__
        if value_type in type_counts:
            type_counts[value_type] += 1
        else:
            type_counts[value_type] = 1
    return type_counts

# Example usage
result = type_count(a=1, b='string', c=1.0, d=True, e=False)
print(result)  # {'int': 1, 'str': 1, 'float': 1, 'bool': 2}
