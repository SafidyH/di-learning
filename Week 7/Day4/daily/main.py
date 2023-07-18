def divide_by_zero():
    try:
        result = 5 / 0
        print("The result is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("An error occurred:", str(e))

# Call the function
divide_by_zero()
