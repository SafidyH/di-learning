import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Box plot of age distribution by gender
sns.catplot(x="Sex", y="Age", data=df, kind="box")
plt.title("Age Distribution by Gender")
plt.show()

# Count plot of survival by class and gender
sns.catplot(x="Pclass", hue="Sex", col="Survived", data=df, kind="count")
plt.suptitle("Survival by Class and Gender")
plt.show()

# Violin plot of fare distribution by class
sns.catplot(x="Pclass", y="Fare", data=df, kind="violin")
plt.title("Fare Distribution by Class")
plt.show()

# Pairplot of numeric features colored by survival
sns.pairplot(df, hue="Survived", diag_kind="hist")
plt.suptitle("Pairplot of Numeric Features Colored by Survival")
plt.show()
