import pandas as pd

df = sns.load_dataset('iris')

# Task 1: Print the 50th row
print("50th row:")
print(df.iloc[49])  # DataFrame index is 0-based

# Task 2: Get rows 50 to 60 skipping every other row
new_df = df.iloc[49:60:2, [4, 2, 3]]  # Columns: species, petal_length, petal_width
print("\nNew DataFrame:")
print(new_df)

# Task 3: Group by species and get median and sum of sepal_length for each group
grouped_data = df.groupby('species')['sepal_length'].agg(['median', 'sum'])
print("\nGrouped data:")
print(grouped_data)
