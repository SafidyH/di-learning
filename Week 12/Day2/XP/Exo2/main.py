import numpy as np

a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])

# Drop NaN values
a_without_nan = a[~np.isnan(a)]

print(a_without_nan)
