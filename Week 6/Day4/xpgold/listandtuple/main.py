# Accept input from the user
numbers = input("Enter comma-separated numbers: ")

# Generate a list by splitting the input string
numbers_list = numbers.split(',')

# Generate a tuple from the list
numbers_tuple = tuple(numbers_list)

# Print the list and tuple
print(numbers_list)
print(numbers_tuple)
