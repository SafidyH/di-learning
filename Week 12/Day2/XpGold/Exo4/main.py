import pandas as pd

# Original wide format dataframe
df = pd.DataFrame({'Name': {0: 'Megane', 1: 'Yonah', 2: 'Avner'},
                   'Course': {0: 'Masters', 1: 'Bachelors', 2: 'Graduate'},
                   'Nationality': {0: "FR", 1: "US", 2: "FR"}})

# Convert to long format using melt()
long_df = pd.melt(df, id_vars=['Name'], value_vars=['Course', 'Nationality'],
                  var_name='Category', value_name='Value')

print("Long Format:")
print(long_df)

# Convert back to wide format using pivot()
wide_df = long_df.pivot(index='Name', columns='Category', values='Value').reset_index()

print("\nWide Format:")
print(wide_df)
