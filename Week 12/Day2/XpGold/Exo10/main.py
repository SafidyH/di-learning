import numpy as np
import time
import matplotlib.pyplot as plt

sizes = [10, 1000, 10000, 50000, 100000, 1000000, 5000000, 10000000]
time_add = []
time_add_arrays = []
time_concatenate = []
time_dot_product = []

for size in sizes:
    # Using Python lists
    list1 = [i for i in range(size)]
    list2 = [i for i in range(size)]
    
    start_time = time.process_time()
    result_list = [x + 5 for x in list1]
    time_add.append(time.process_time() - start_time)
    
    start_time = time.process_time()
    result_add = [a + b for a, b in zip(list1, list2)]
    time_add_arrays.append(time.process_time() - start_time)
    
    start_time = time.process_time()
    result_concatenate = list1 + list2
    time_concatenate.append(time.process_time() - start_time)
    
    # Using NumPy arrays
    array1 = np.arange(size)
    array2 = np.arange(size)
    
    start_time = time.process_time()
    result_array = array1 + 5
    time_add.append(time.process_time() - start_time)
    
    start_time = time.process_time()
    result_add_arrays = array1 + array2
    time_add_arrays.append(time.process_time() - start_time)
    
    start_time = time.process_time()
    result_concatenate = np.concatenate((array1, array2))
    time_concatenate.append(time.process_time() - start_time)
    
    start_time = time.process_time()
    result_dot_product = np.dot(array1, array2)
    time_dot_product.append(time.process_time() - start_time)

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(sizes, time_add, label='List')
plt.plot(sizes, time_add_arrays, label='NumPy')
plt.title('Time for Adding 5')
plt.xlabel('Array Size')
plt.ylabel('Time')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(sizes, time_add_arrays, label='List')
plt.plot(sizes, time_add_arrays, label='NumPy')
plt.title('Time for Adding Arrays')
plt.xlabel('Array Size')
plt.ylabel('Time')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(sizes, time_concatenate, label='List')
plt.plot(sizes, time_concatenate, label='NumPy')
plt.title('Time for Concatenation')
plt.xlabel('Array Size')
plt.ylabel('Time')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(sizes, time_dot_product, label='List')
plt.plot(sizes, time_dot_product, label='NumPy')
plt.title('Time for Dot Product')
plt.xlabel('Array Size')
plt.ylabel('Time')
plt.legend()

plt.tight_layout()
plt.show()
