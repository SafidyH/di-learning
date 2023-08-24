import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the Cars93 dataset from the provided URL
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
cars93_df = pd.read_csv(url)

# Define the target variable
target_variable = 'Price'

# Define categorical and continuous features
categorical_features = ['Manufacturer', 'Model', 'Type', 'AirBags', 'DriveTrain', 'Cylinders', 'Man.trans.avail', 'Origin']
continuous_features = ['MPG.city', 'MPG.highway', 'EngineSize', 'Horsepower', 'RPM', 'Rev.per.mile', 'Fuel.tank.capacity', 'Passengers', 'Length', 'Wheelbase', 'Width', 'Turn.circle', 'Weight']

# Explore the data
print("Summary Statistics:")
print(cars93_df.describe())
print("\nMissing Values:")
print(cars93_df.isnull().sum())

# Handling missing values
cars93_df.fillna(cars93_df.median(), inplace=True)  # Fill missing values with median for continuous features

# Examine correlated features and plot correlations
correlation_matrix = cars93_df[continuous_features + [target_variable]].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# Extract new features
cars93_df['Married'] = cars93_df['Manufacturer'].str.contains("Mr\.|Mrs\.", regex=True)
print("Unique values in 'Married':", cars93_df['Married'].unique())

# Extract and plot features with the target variable
plt.figure(figsize=(12, 10))
for feature in continuous_features:
    plt.subplot(4, 4, continuous_features.index(feature) + 1)
    sns.scatterplot(data=cars93_df, x=feature, y=target_variable)
    plt.title(f'{feature} vs {target_variable}')
plt.tight_layout()
plt.show()
