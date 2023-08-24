import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the Titanic dataset from the provided URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# Define categorical and continuous features
categorical_features = ['Pclass', 'Sex', 'Embarked']
ordinal_categorical_features = ['Pclass']  # Ordinal categorical features
nominal_categorical_features = ['Sex', 'Embarked']  # Nominal categorical features
continuous_features = ['Age', 'Fare', 'SibSp', 'Parch']

# Explore the data
print("Summary Statistics:")
print(titanic_df.describe())
print("\nMissing Values:")
print(titanic_df.isnull().sum())

# Plot distributions of features
plt.figure(figsize=(12, 8))
for feature in continuous_features:
    sns.histplot(data=titanic_df, x=feature, bins=20, kde=True)
    plt.title(f'Distribution of {feature}')
    plt.show()

# Plot relationships with target variable
plt.figure(figsize=(12, 8))
sns.boxplot(data=titanic_df, x='Pclass', y='Fare', hue='Survived')
plt.title('Fare by Pclass and Survival')
plt.show()

# Process the data
# Handling missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0], inplace=True)

# Convert categorical features to numeric
titanic_df['Sex'] = titanic_df['Sex'].map({'female': 0, 'male': 1})
titanic_df['Embarked'] = titanic_df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Remove columns that are not important (e.g., 'Name', 'Ticket', 'Cabin')
titanic_df.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Split data into train and test sets
X = titanic_df.drop('Survived', axis=1)
y = titanic_df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Train set shape:", X_train.shape)
print("Test set shape:", X_test.shape)
