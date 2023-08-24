import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def line_plot(df):
    toyota_df = df[df['car_name'].str.contains('toyota', case=False)]
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='model_year', y='weight', data=toyota_df)
    plt.xlabel('Model Year')
    plt.ylabel('Weight')
    plt.title('Change in Weight over Years for Toyota Cars')
    plt.tight_layout()
    plt.show()

# Example usage with df_mpg dataframe
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

line_plot(df_mpg)
