import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def bar_plot(df):
    filtered_df = df[(df['model_year'] == 78) & (df['car_name'].str.contains('toyota', case=False))]

    plt.figure(figsize=(10, 6))
    sns.barplot(x='car_name', y='cylinders', data=filtered_df)
    plt.xlabel('Car Name')
    plt.ylabel('Cylinders')
    plt.title('Cylinders Comparison for 1978 Toyota Cars')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Example usage with df_mpg dataframe
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

bar_plot(df_mpg)
