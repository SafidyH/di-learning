import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the URL
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

# Drop rows with NaN values in specified columns
df_cleaned = df.dropna(subset=['RPM', 'Type', 'Price'])

# Create a scatter plot
plt.figure(figsize=(10, 6))

# Plotting for each car type separately
for car_type in df_cleaned['Type'].unique():
    type_data = df_cleaned[df_cleaned['Type'] == car_type]
    plt.scatter(type_data['RPM'], type_data['Price'], label=car_type)

# Adding labels, title, and legend
plt.xlabel('RPM')
plt.ylabel('Price')
plt.title('Relation between RPM and Price')
plt.legend()

# Show the plot
plt.show()
