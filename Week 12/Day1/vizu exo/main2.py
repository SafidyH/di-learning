import numpy as np
import matplotlib.pyplot as plt

# Create an array of length 100 with random integers between 0 and 75
random_array = np.random.randint(0, 76, size=100)

# Reshape the array to a 50x2 matrix
reshaped_array = random_array.reshape(50, 2)

# Scatter plot of the 1st column as x and the 2nd column as y
plt.scatter(reshaped_array[:, 0], reshaped_array[:, 1])
plt.xlabel('1st Column')
plt.ylabel('2nd Column')
plt.title('Scatter Plot of 1st vs 2nd Column')
plt.show()

# Histogram of each column with titles
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(reshaped_array[:, 0], bins=10, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 1st Column')

plt.subplot(1, 2, 2)
plt.hist(reshaped_array[:, 1], bins=10, color='green', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 2nd Column')

plt.tight_layout()
plt.show()
