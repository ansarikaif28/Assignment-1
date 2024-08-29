import time
import random
import pandas as pd
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Random lists of different sizes
input_sizes = [1000,2000,3000,4000]

#List of the Execution times for the different execution times
execution_times = []

#List of the unsorted numbers
unsorted_arrays = []

#List of sorted numbers
sorted_arrays = []

for size in input_sizes:

    # Generating an array of random numbers based on the input size
    arr = random.sample(range(10000), size)

    unsorted_arrays.append(arr.copy())  # Store the unsorted array
    start_time = time.time()

    #sorting the array of numbers
    bubble_sort(arr)

    end_time = time.time()

    execution_times.append(end_time - start_time)# Store the different execution time of different input size

    sorted_arrays.append(arr)  # Store the sorted array



# Print the unsorted and sorted arrays
for size, unsorted_arr, sorted_arr in zip(input_sizes, unsorted_arrays, sorted_arrays):
    print(f"\nUnsorted array of size {size}:")
    print(", ".join(map(str, unsorted_arr[:4])) + ", ..., " + ", ".join(map(str, unsorted_arr[-4:])))
    print(f"Sorted array of size {size}:")
    print(", ".join(map(str, sorted_arr[:4])) + ", ..., " + ", ".join(map(str, sorted_arr[-4:])))

# Print the results

df = pd.DataFrame({
    'Input Size': input_sizes,
    'Execution Time (seconds)': execution_times
})

# Print the DataFrame
print()
print()
print(df.to_string(index = False))

import time
import random
import pandas as pd
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sizes of the input arrays
input_sizes = [1000, 2000, 3000, 4000]

# Lists to store execution times, unsorted arrays, and sorted arrays
execution_times = []
unsorted_arrays = []
sorted_arrays = []

# Perform sorting and time the execution
for size in input_sizes:
    arr = random.sample(range(10000), size)  # Generate unique random numbers
    unsorted_arrays.append(arr.copy())  # Store the unsorted array
    
    start_time = time.time()
    bubble_sort(arr)  # Sort the array
    end_time = time.time()
    
    execution_times.append(end_time - start_time)  # Record the execution time
    sorted_arrays.append(arr)  # Store the sorted array

# Print a summary of unsorted and sorted arrays
for size, unsorted_arr, sorted_arr in zip(input_sizes, unsorted_arrays, sorted_arrays):
    print(f"\nUnsorted array of size {size}:")
    print(", ".join(map(str, unsorted_arr[:4])) + ", ..., " + ", ".join(map(str, unsorted_arr[-4:])))
    print(f"Sorted array of size {size}:")
    print(", ".join(map(str, sorted_arr[:4])) + ", ..., " + ", ".join(map(str, sorted_arr[-4:])))

# Create a DataFrame for the results
df = pd.DataFrame({
    'Input Size': input_sizes,
    'Execution Time (seconds)': execution_times
})

# Print the DataFrame
print()
print(df.to_string(index=False))

# Plot a pie chart
plt.figure(figsize=(8, 8))
plt.pie(df['Execution Time (seconds)'], labels=df['Input Size'], autopct='%1.1f%%', startangle=140)
plt.title('Bubble Sort Execution Time by Input Size')
plt.show()
