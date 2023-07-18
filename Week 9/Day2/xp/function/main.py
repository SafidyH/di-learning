def built_in_functions_demo():
    """
    This program demonstrates the usage of Python built-in functions.

    Functions demonstrated:
    1. abs(): Returns the absolute value of a number.
    2. int(): Converts a value to an integer.
    3. input(): Reads input from the user.

    Execution:
    - The program prompts the user to enter a number.
    - It calculates and prints the absolute value of the number using the abs() function.
    - Then, it prompts the user to enter a value.
    - It converts the value to an integer using the int() function and prints the result.

    Note: The program assumes that the user will enter a valid number or value.

    """

    # Prompt the user to enter a number
    number = float(input("Enter a number: "))

    # Calculate and print the absolute value of the number
    absolute_value = abs(number)
    print("Absolute value:", absolute_value)

    # Prompt the user to enter a value
    value = input("Enter a value: ")

    # Convert the value to an integer and print the result
    integer_value = int(value)
    print("Integer value:", integer_value)


# Call the function to run the program
built_in_functions_demo()
