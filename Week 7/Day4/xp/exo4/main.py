def calculate_sum(X):
    # Convert X to a string to concatenate the digits
    X_str = str(X)
    # Calculate the values of X, XX, XXX, XXXX
    X_value = int(X_str)
    XX_value = int(X_str + X_str)
    XXX_value = int(X_str + X_str + X_str)
    XXXX_value = int(X_str + X_str + X_str + X_str)
    # Calculate the sum of the values
    sum_value = X_value + XX_value + XXX_value + XXXX_value
    return sum_value

# Test the function
X = 3
result = calculate_sum(X)
print(result)
