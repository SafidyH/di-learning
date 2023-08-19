import random
import string

def generate_random_string(length=5):
    # Define the pool of characters (uppercase and lowercase letters)
    letters = string.ascii_letters

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(letters) for _ in range(length))

    return random_string

# Example usage:
random_string = generate_random_string()
print(random_string)
