x = int(input('Enter the Number:')) 
def is_perfect_number(number):
    # Initialize the sum of divisors to 0
    divisor_sum = 0

    # Find the divisors of the number and calculate their sum
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    # Check if the sum of divisors is equal to the number
    if divisor_sum == number:
        return True
    else:
        return False

# Ask the user for a number
number = int(input("Enter the number: "))

# Check if the number is perfect and print the result
is_perfect = is_perfect_number(number)
print(is_perfect)
