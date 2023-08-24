import pandas as pd

# Read the data from the URL
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# Calculate the absolute tip amounts
df['abs_tip'] = abs(df['tip'])

# Find the row with the maximum absolute tip
max_tip_row = df[df['abs_tip'] == df['abs_tip'].max()]

# Extract the day and time from the row
most_tip_day = max_tip_row['day'].values[0]
most_tip_time = max_tip_row['time'].values[0]

print("Day with the Most Tip:", most_tip_day)
print("Time with the Most Tip:", most_tip_time)
