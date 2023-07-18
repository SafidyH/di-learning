import random

# Generate a list of 10 random integers between -100 and 100
numbers = random.sample(range(-100, 101), 10)

# Print the original list of numbers
print("Original list:", numbers)

# Sort the numbers in descending order
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted list (descending):", sorted_numbers)

# Calculate the sum of all the numbers
sum_of_numbers = sum(numbers)
print("Sum of all numbers:", sum_of_numbers)

# Create a list containing the first and the last numbers
first_last_numbers = [numbers[0], numbers[-1]]
print("First and last numbers:", first_last_numbers)

# Create a list of numbers greater than 50
greater_than_50 = [num for num in numbers if num > 50]
print("Numbers greater than 50:", greater_than_50)

# Create a list of numbers smaller than 10
smaller_than_10 = [num for num in numbers if num < 10]
print("Numbers smaller than 10:", smaller_than_10)

# Create a list of squared numbers
squared_numbers = [num ** 2 for num in numbers]
print("Squared numbers:", ' '.join(map(str, squared_numbers)))

# Create a list of numbers without duplicates
unique_numbers = list(set(numbers))
print("Numbers without duplicates:", unique_numbers)
print("Count of unique numbers:", len(unique_numbers))

# Calculate the average of all the numbers
average = sum_of_numbers / len(numbers)
print("Average of all numbers:", average)

# Find the largest number
largest_number = max(numbers)
print("Largest number:", largest_number)

# Find the smallest number
smallest_number = min(numbers)
print("Smallest number:", smallest_number)

# Bonus: Find the sum, average, largest, and smallest number without using built-in functions
# Sum without using sum()
sum_without_builtin = 0
for num in numbers:
    sum_without_builtin += num
print("Sum without using built-in function:", sum_without_builtin)

# Average without using len() or sum()
count = 0
total = 0
for num in numbers:
    count += 1
    total += num
average_without_builtin = total / count
print("Average without using built-in functions:", average_without_builtin)

# Largest number without using max()
largest_number_without_builtin = numbers[0]
for num in numbers:
    if num > largest_number_without_builtin:
        largest_number_without_builtin = num
print("Largest number without using built-in function:", largest_number_without_builtin)

# Smallest number without using min()
smallest_number_without_builtin = numbers[0]
for num in numbers:
    if num < smallest_number_without_builtin:
        smallest_number_without_builtin = num
print("Smallest number without using built-in function:", smallest_number_without_builtin)
