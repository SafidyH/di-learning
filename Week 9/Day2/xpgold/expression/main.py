import re

def return_numbers(input_string):
    # Use regex to find all occurrences of digits in the input string
    numbers_list = re.findall(r'\d', input_string)

    # Join the list of numbers and convert it to an integer
    result = int(''.join(numbers_list))

    return result

# Example usage:
input_string = 'k5k3q2g5z6x9bn'
result = return_numbers(input_string)
print("Expected output:", result)
