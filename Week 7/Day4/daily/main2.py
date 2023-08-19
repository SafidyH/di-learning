def compute_division():
    try:
        result = 5 / 0
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

if __name__ == "__main__":
    result = compute_division()
    if result is not None:
        print("Result of 5/0 =", result)
