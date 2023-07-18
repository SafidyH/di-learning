def custom_split(string, delimiter=None):
    if delimiter is None:
        return string.split()
    else:
        return string.split(delimiter)

# Example usage
text = "Hello, World!"
result = custom_split(text)
print(result)  # ['Hello,', 'World!']

result = custom_split(text, ',')
print(result)  # ['Hello', ' World!']
