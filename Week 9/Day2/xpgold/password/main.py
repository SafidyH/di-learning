import random
import string

def is_valid_password(password):
    # Check if the password length is between 6 and 30 characters
    if not 6 <= len(password) <= 30:
        return False

    # Check if the password contains at least one digit, lowercase, uppercase, and special character
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in string.punctuation for char in password)

    return has_digit and has_lower and has_upper and has_special

def generate_password(length):
    # Define the character sets for each type of character
    digits = string.digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    special_characters = string.punctuation

    # Generate a password with at least one of each type of character
    password = random.choice(digits) + random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(special_characters)

    # Generate the rest of the password with random characters from all the sets
    remaining_length = length - 4
    password += ''.join(random.choice(digits + lowercase_letters + uppercase_letters + special_characters) for _ in range(remaining_length))

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def test_password_generation():
    for _ in range(100):
        password_length = random.randint(6, 30)
        password = generate_password(password_length)
        print("Generated password:", password)
        if is_valid_password(password):
            print("Password is valid.")
        else:
            print("Password is NOT valid.")

test_password_generation()
