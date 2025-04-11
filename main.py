import matplotlib.pyplot as plt
import pandas as pd

from utils.supports import measure_execution_time, generate_array_with_duplicates, generate_large_array
from algorithms.selectionSort import selectionSort
from algorithms.hasDuplicates import hasDuplicates
from algorithms.allPairs import allPairs

def main():
    input_sizes = [50 * i for i in range(1, 21)]

    sort_times = []
    duplicate_times = []
    pair_times = []

    for size in input_sizes:
        large_array = generate_large_array(size)
        duplicates = generate_array_with_duplicates(size)
        pairs = generate_large_array(size)

        sort_time = measure_execution_time(selectionSort, large_array)
        sort_times.append(sort_time)

        duplicate_time = measure_execution_time(hasDuplicates, duplicates)
        duplicate_times.append(duplicate_time)

        pair_time = measure_execution_time(allPairs, pairs)
        pair_times.append(pair_time)

        print(f"Computed size {size}")

    data = {
        "Input Size": input_sizes,
        "Selection Sort Time": sort_times,
        "Duplicate Check Time": duplicate_times,
        "All Pairs Time": pair_times,
    }
    df = pd.DataFrame(data)
    print(df)

    plt.figure(figsize=(10, 6))
    plt.plot(df["Input Size"], df["Selection Sort Time"], label="Selection Sort", marker="o")
    plt.plot(df["Input Size"], df["Duplicate Check Time"], label="Has Duplicates", marker="s")
    plt.plot(df["Input Size"], df["All Pairs Time"], label="All Pairs", marker="^")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time of O(n^2) Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show(block=True)

if __name__ == "__main__":
    main()