import math

def norm(lst):
    sum_of_squares = sum([x ** 2 for x in lst])
    l2_norm = math.sqrt(sum_of_squares)
    return l2_norm

# Test the function
lst = [1, 2, 2]
result = norm(lst)
print(result)
