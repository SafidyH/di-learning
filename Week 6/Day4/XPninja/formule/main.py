import math

C = 50
H = 30

numbers = input("Enter comma-separated numbers: ")

numbers_list = numbers.split(',')

results = []
for num in numbers_list:
    D = int(num)
    Q = math.sqrt((2 * C * D) / H)
    results.append(round(Q))

results_str = ','.join(map(str, results))

print(results_str)
