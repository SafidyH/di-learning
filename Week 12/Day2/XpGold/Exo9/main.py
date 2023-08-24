import numpy as np
import matplotlib.pyplot as plt

# Create a figure with 5 subplots
fig, axes = plt.subplots(1, 5, figsize=(15, 3))

# Define different functions and colors
functions = [np.sin, np.cos, np.exp, np.log, np.tan]
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Plot each function in a different subplot
for i, (func, color) in enumerate(zip(functions, colors)):
    x = np.linspace(0, 10, 100)
    y = func(x)
    axes[i].plot(x, y, color=color)
    axes[i].set_title(func.__name__)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('y')

# Adjust layout and show the first set of subplots
plt.tight_layout()
plt.show()

# Create another set of subplots with shared axes
fig, axes = plt.subplots(1, 5, figsize=(15, 3), sharex=True, sharey=True)

# Plot each function with shared axes
for i, (func, color) in enumerate(zip(functions, colors)):
    x = np.linspace(0, 10, 100)
    y = func(x)
    axes[i].plot(x, y, color=color)
    axes[i].set_title(func.__name__)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('y')

# Adjust layout and show the second set of subplots
plt.tight_layout()
plt.show()
