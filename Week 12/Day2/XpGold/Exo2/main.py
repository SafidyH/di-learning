import numpy as np

x = np.arange(100)
limited_array = np.clip(x, 20, 80)

print(limited_array)
