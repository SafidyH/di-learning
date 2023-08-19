import random

def roll_and_compare(user_number):
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # Check if the user's number and the random number are the same
    if user_number == random_number:
        print("Success! The random number ({}) matches your number ({}).".format(random_number, user_number))
    else:
        print("Try again! The random number was {}.".format(random_number))

#call function
roll_and_compare(50)
