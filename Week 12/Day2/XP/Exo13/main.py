import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the auto-mpg data
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

# Scatter plot of 'horsepower' vs 'mpg'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='horsepower', y='mpg', data=df_mpg)
plt.xlabel('Horsepower')
plt.ylabel('Miles per Gallon')
plt.title('Relationship between Horsepower and Fuel Efficiency')
plt.tight_layout()
plt.show()
