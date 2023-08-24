import pandas as pd

# Read the data from the URL
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# Calculate the average percent of tips for women
avg_tip_percent_women = df[df['sex'] == 'Female']['tip'] / df[df['sex'] == 'Female']['total_bill'] * 100
avg_tip_percent_women = avg_tip_percent_women.mean()

# Calculate the average percent of tips for men
avg_tip_percent_men = df[df['sex'] == 'Male']['tip'] / df[df['sex'] == 'Male']['total_bill'] * 100
avg_tip_percent_men = avg_tip_percent_men.mean()

# Create a dataframe to present the data
data = {'Gender': ['Women', 'Men'],
        'Average Tip Percent': [avg_tip_percent_women, avg_tip_percent_men]}
result_df = pd.DataFrame(data)

print(result_df)
