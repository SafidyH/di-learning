def common_div(num1, num2):
    divisors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return divisors

# Example usage
result = common_div(10, 20)
print(result)  # [1, 2, 5, 10]
