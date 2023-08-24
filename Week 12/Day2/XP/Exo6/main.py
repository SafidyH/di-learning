import pandas as pd

data_url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"


# Read the data from the CSV file into a Pandas DataFrame
data = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv")

# Print how many columns are of each datatype
datatype_counts = data.dtypes.value_counts()
print("Columns by Datatype:")
print(datatype_counts)

# Change the column name "Type" to "TypeOfCar"
data.rename(columns={"Type": "TypeOfCar"}, inplace=True)

# Print the head of the DataFrame after renaming
print("\nHead of DataFrame:")
print(data.head())

# Count the missing values in each column
missing_values_count = data.isnull().sum()
print("\nMissing Values Count:")
print(missing_values_count)

# Find the column with the most missing values
most_missing_column = missing_values_count.idxmax()
print("\nColumn with Most Missing Values:", most_missing_column)
