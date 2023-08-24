from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Boston housing dataset
boston = load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['Price'] = boston.target

# List of continuous features
continuous_features = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

# Plot boxplots of each continuous feature
plt.figure(figsize=(12, 8))
for feature in continuous_features:
    sns.boxplot(x=boston_df[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()

# Calculate outliers using 1.5 * IQR rule
outliers_count = {}
for feature in continuous_features:
    q1 = np.percentile(boston_df[feature], 25)
    q3 = np.percentile(boston_df[feature], 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers_count[feature] = len(boston_df[(boston_df[feature] < lower_bound) | (boston_df[feature] > upper_bound)])

# Print the count of outliers for each feature
print("Outliers count:")
for feature, count in outliers_count.items():
    print(f"{feature}: {count} outliers")
