import numpy as np

a = np.arange(30)
b = a.reshape((7, 6))
c = np.ones((5, 6, 3))

# Multiplication 1: 5x6 matrix from c multiplied by a row vector from a
result_1 = c[:, :, 0] * a[:6]
print("Multiplication 1:")
print("Result:")
print(result_1)
print("Shape:", result_1.shape)

# Multiplication 2: 5x6 matrix from c multiplied by a column vector from a
result_2 = c[:, :, 0] * a[:30:6].reshape(-1, 1)
print("\nMultiplication 2:")
print("Result:")
print(result_2)
print("Shape:", result_2.shape)

# Multiplication 3: 6x3 matrix from b multiplied by c
result_3 = b[:6] * c[0]
print("\nMultiplication 3:")
print("Result:")
print(result_3)
print("Shape:", result_3.shape)

# Multiplication 4: 5x6 matrix from b multiplied by c
result_4 = b[:5] * c[0]
print("\nMultiplication 4:")
print("Result:")
print(result_4)
print("Shape:", result_4.shape)
