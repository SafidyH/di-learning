import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Explore the data
print("First Few Rows:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())
print("\nData Information:")
print(df.info())

# Visualize the data
# Pie chart for gender distribution
gender_counts = df['Sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.show()

# Histogram for passenger ages
plt.figure(figsize=(8, 6))
plt.hist(df['Age'].dropna(), bins=20, edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Passenger Age Distribution')
plt.show()

# Bar plot for survival
survived_counts = df['Survived'].value_counts()
plt.figure(figsize=(6, 6))
plt.bar(survived_counts.index, survived_counts.values)
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.xlabel('Survival')
plt.ylabel('Count')
plt.title('Survival Count')
plt.show()

# Stacked bar plot for survival by gender
survival_gender = df.groupby(['Survived', 'Sex']).size().unstack()
survival_gender.plot(kind='bar', stacked=True)
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.xlabel('Survival')
plt.ylabel('Count')
plt.title('Survival by Gender')
plt.show()

# Scatter plot for fare and age
plt.figure(figsize=(8, 6))
plt.scatter(df['Fare'], df['Age'], alpha=0.5)
plt.xlabel('Fare')
plt.ylabel('Age')
plt.title('Fare vs Age')
plt.show()

# Preprocess the data
# Handle missing values in 'Age' column
df['Age'].fillna(df['Age'].median(), inplace=True)

# Normalize the 'Fare' column using Min-Max scaling
df['Fare'] = (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())

# Convert 'Sex' column to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)

# Data Analysis
# Calculate survival rate by gender
survival_rate_gender = df.groupby('Sex_male')['Survived'].mean()
print("\nSurvival Rate by Gender:")
print(survival_rate_gender)

# Calculate survival rate by passenger class
survival_rate_class = df.groupby('Pclass')['Survived'].mean()
print("\nSurvival Rate by Passenger Class:")
print(survival_rate_class)

# Identify passenger with the highest fare
passenger_highest_fare = df[df['Fare'] == df['Fare'].max()]
print("\nPassenger with the Highest Fare:")
print(passenger_highest_fare)
