import pandas as pd

data_url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
# Read the data from the CSV file into a Pandas DataFrame
data = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv")

# Display the DataFrame before deletion
print("DataFrame before deletion:")
print(data.head())

# Method 1: Using the .drop() method
data_without_engine_size = data.drop(columns=["EngineSize"])
data_without_length = data.drop(columns=["Length"])

# Display the DataFrame after deletion
print("\nDataFrame after deletion using .drop() method:")
print(data_without_engine_size.head())
print(data_without_length.head())

# Method 2: Using the del statement
del data["EngineSize"]
del data["Length"]

# Display the DataFrame after deletion using del
print("\nDataFrame after deletion using del statement:")
print(data.head())
