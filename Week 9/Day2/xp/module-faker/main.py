from faker import Faker

# Create an instance of Faker
fake = Faker()

# Create an empty list to store user dictionaries
users = []

# Function to add new user dictionaries to the users list
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

# Example usage:
add_user()
add_user()
add_user()

# Print the list of users
print(users)
