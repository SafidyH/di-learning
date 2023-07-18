matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

# Determine the number of columns
num_columns = len(matrix[0])

# Create an empty list for the decoded message
decoded_message = []

# Iterate over the columns
for column in range(num_columns):
    # Iterate over the rows
    for row in range(len(matrix)):
        # Get the character at the current position
        char = matrix[row][column]
        
        # Check if the character is alphanumeric
        if char.isalnum():
            decoded_message.append(char)
        else:
            decoded_message.append(" ")

# Join the decoded message list into a string
secret_message = ''.join(decoded_message)

# Print the secret message
print(secret_message)
