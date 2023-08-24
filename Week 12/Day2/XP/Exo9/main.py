import pandas as pd

data = ["STD,City\tState",
        "33,Kolkata\tWest Bengal",
        "44,Chennai\tTamil Nadu",
        "40,Hyderabad\tTelengana",
        "80,Bangalore\tKarnataka"]

df = pd.DataFrame(data, columns=['row'])

# Split the "row" column and create a new dataframe
split_data = df['row'].str.split('[,\t]', expand=True)
split_data.columns = ['STD', 'City', 'State']

print(split_data)

names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

# Display the first few rows of the df_mpg dataframe
print(df_mpg.head())
