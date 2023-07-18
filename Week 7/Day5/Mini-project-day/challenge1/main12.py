def is_palindrome(string):
    # Convert the string to lowercase and remove whitespace
    string = string.lower().replace(" ", "")
    
    # Check if the reversed string is equal to the original string
    return string == string[::-1]

# Example usage
print(is_palindrome('radar'))  # True
print(is_palindrome('John'))   # False
