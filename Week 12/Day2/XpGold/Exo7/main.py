import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the DataFrame
df = pd.DataFrame({'x': range(1, 11),
                   'y_1': np.random.randn(10),
                   'y_2': np.random.randn(10) + range(1, 11),
                   'y_3': np.random.randn(10) + range(11, 21)})

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot y_1 with blue 'o' markers
ax.plot(df['x'], df['y_1'], 'bo', markersize=8, label='y_1', linewidth=4)

# Plot y_2 with a red line
ax.plot(df['x'], df['y_2'], color='red', label='y_2', linewidth=4)

# Plot y_3 with a green dashed line and a legend
ax.plot(df['x'], df['y_3'], color='green', linestyle='--', label='y_3', linewidth=2)

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Trend Plots')

# Add legend
ax.legend()

# Show the plot
plt.show()
