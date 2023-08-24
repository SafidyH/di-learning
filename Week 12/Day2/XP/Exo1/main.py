import numpy as np

def create_array(start, length, stop):
    step = (stop - start) / (length - 1)
    return np.arange(start, stop + step, step)

start = 6
length = 100
stop = start + (length - 1) * 4

result_array = create_array(start, length, stop)
print(result_array)
