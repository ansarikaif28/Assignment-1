import time
import random
import pandas as pd
import cProfile
import pstats

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
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

    # Create a DataFrame for the results
    df = pd.DataFrame({
        'Input Size': input_sizes,
        'Execution Time (seconds)': execution_times
    })

    # Print the DataFrame
    print()
    print(df.to_string(index=False))

# Profile the code and save results
if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()

    # Save profiling results to a file
    with open("profile_output.prof", "w") as f:
        profiler.dump_stats("profile_output.prof")

    # Print profiling results to the console
    stats = pstats.Stats(profiler)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()