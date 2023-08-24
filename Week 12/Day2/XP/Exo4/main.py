import pandas as pd
import numpy as np

# Create the Pandas Series
series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))

# Find unique values and their frequencies
unique_values = series.value_counts()

print(unique_values)
