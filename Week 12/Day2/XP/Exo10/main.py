import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def scatter_plot(df):
    sns.scatterplot(x='displacement', y='acceleration', data=df)
    plt.xlabel('Displacement')
    plt.ylabel('Acceleration')
    plt.title('Scatter Plot of Displacement vs Acceleration')
    plt.show()

# Example usage with df_mpg dataframe
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

scatter_plot(df_mpg)
