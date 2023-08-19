def calculate_sum(X):
    if not isinstance(X, int) or X < 0:
        raise ValueError("Input must be a positive integer.")

    X_str = str(X)
    total_sum = X
    current_term = X

    for i in range(1, 4):
        current_term = int(X_str * (i + 1))
        total_sum += current_term

    return total_sum

if __name__ == "__main__":
    try:
        X = int(input("Enter a positive integer: "))
        result = calculate_sum(X)
        print(f"The result of {X} + {X}{X} + {X}{X}{X} + {X}{X}{X}{X} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
