import random

def compare_numbers(number):
    random_number = random.randint(1, 100)
    
    if number == random_number:
        print("Success! The numbers match.")
    else:
        print("Fail! The numbers don't match.")
        print("Given number:", number)
        print("Random number:", random_number)

# Call the function with a number
compare_numbers(50)
