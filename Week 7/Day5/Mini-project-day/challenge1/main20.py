def convert_to_password(string):
    password = '*' * len(string)
    return password

# Example usage
input_string = "mypassword"
output_password = convert_to_password(input_string)
print(output_password)  # ***********
