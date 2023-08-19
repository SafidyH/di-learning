import re

def validate_full_name(full_name):
    # Check if the name contains only letters and one space
    if not re.match(r'^[A-Za-z]+ [A-Za-z]+$', full_name):
        return False

    # Check if the first letter of each name is upper-cased
    names = full_name.split()
    for name in names:
        if not name[0].isupper():
            return False

    return True

# Ask the user for their full name
user_full_name = input("Please enter your full name: ")

# Validate the full name
is_valid_name = validate_full_name(user_full_name)

# Display the result
if is_valid_name:
    print("Valid name!")
else:
    print("Invalid name. Please enter a valid full name with only letters and one space, with the first letter of each name in upper case.")
