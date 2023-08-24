import pandas as pd
import numpy as np

# Create the first dataframe
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

# Create the second dataframe
df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

# Merge dataframes by two columns
merged_df = pd.merge(df1, df2, left_on=['fruit', 'weight'], right_on=['pazham', 'kilo'])

# Drop duplicate columns
merged_df = merged_df.drop(columns=['pazham', 'kilo'])

print(merged_df)
