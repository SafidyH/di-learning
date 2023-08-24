import numpy as np
import random

# Define the dimensions of the table
M = random.randint(2, 49)
N = random.randint(2, 39)

# Create a table filled with random integers
table_list = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
table_numpy = np.random.randint(1, 100, (M, N))

# Print the third row
print("Third Row (Python List):", table_list[2])
print("Third Row (NumPy):", table_numpy[2])

# Print the third column
print("Third Column (Python List):", [row[2] for row in table_list])
print("Third Column (NumPy):", table_numpy[:, 2])

# Set every element in the last row equal to 7
table_list[-1] = [7] * N
table_numpy[-1, :] = 7

# Calculate the sum of the first two columns
sum_columns = [sum(row[:2]) for row in table_list]

# Set every element in the last column equal to the sum
for i in range(M):
    table_list[i][-1] = sum_columns[i]
table_numpy[:, -1] = sum_columns

print("Table (Python List) after modifications:")
for row in table_list:
    print(row)

print("\nTable (NumPy) after modifications:")
print(table_numpy)
