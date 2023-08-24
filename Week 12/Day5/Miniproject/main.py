import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.preprocessing import MinMaxScaler

# Load the Boston Housing dataset
boston = load_boston()
data = pd.DataFrame(boston.data, columns=boston.feature_names)
data['MEDV'] = boston.target

# Explore the data
print("Summary Statistics:")
print(data.describe())
print("\nFirst Few Rows:")
print(data.head())
print("\nData Information:")
print(data.info())

# Create histograms for each column
data.hist(bins=20, figsize=(12, 10))
plt.show()

# Create scatter plots comparing variables with house price (MEDV)
for feature in boston.feature_names:
    plt.scatter(data[feature], data['MEDV'])
    plt.xlabel(feature)
    plt.ylabel('MEDV')
    plt.title(f'{feature} vs MEDV')
    plt.show()

# Preprocess the data
# Identify and address missing data
print("Missing Data:")
print(data.isnull().sum())
# No missing data in the dataset

# Normalize continuous variables
scaler = MinMaxScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

# Create a fake categorical variable
data_scaled['AGE_category'] = pd.cut(data_scaled['AGE'], bins=[0, 0.25, 0.5, 0.75, 1], labels=['very young', 'young', 'middle-aged', 'old'])
data_encoded = pd.get_dummies(data_scaled, columns=['AGE_category'], drop_first=True)

# Correlations
correlation_matrix = data_encoded.corr()
plt.figure(figsize=(12, 10))
plt.title('Correlation Heatmap')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Feature Engineering
data_encoded['RM_LSTAT_product'] = data_encoded['RM'] * data_encoded['LSTAT']

# Analyze property age vs median value
plt.figure(figsize=(12, 8))
plt.hist(data_encoded[data_encoded['AGE_category_old'] == 1]['MEDV'], bins=20, alpha=0.5, label='Old Properties')
plt.hist(data_encoded[data_encoded['AGE_category_middle-aged'] == 1]['MEDV'], bins=20, alpha=0.5, label='Middle-Aged Properties')
plt.hist(data_encoded[data_encoded['AGE_category_young'] == 1]['MEDV'], bins=20, alpha=0.5, label='Young Properties')
plt.hist(data_encoded[data_encoded['AGE_category_very young'] == 1]['MEDV'], bins=20, alpha=0.5, label='Very Young Properties')
plt.xlabel('Median Value (MEDV)')
plt.ylabel('Frequency')
plt.title('Property Age vs Median Value')
plt.legend()
plt.show()

# Analyze neighborhood crime rate impact on prices
data_encoded['CRIM_BIN'] = pd.cut(data_encoded['CRIM'], bins=[0, 1, 5, 10, 20, max(data_encoded['CRIM'])], labels=['0-1', '1-5', '5-10', '10-20', '20+'])
avg_MEDV_per_CRIM_BIN = data_encoded.groupby('CRIM_BIN')['MEDV'].mean()
plt.figure(figsize=(10, 6))
avg_MEDV_per_CRIM_BIN.plot(kind='line', marker='o')
plt.xlabel('Binned Crime Rate')
plt.ylabel('Average MEDV')
plt.title('Neighborhood Crime Rate Impact on Prices')
plt.xticks(rotation=45)
plt.grid()
plt.show()
