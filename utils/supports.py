import time
import random

def measure_execution_time(algorithm, *args):
    """
    Measure the execution time of an algorithm.
    :param algorithm: The algorithm to measure.
    :param args: Arguments to pass to the algorithm.
    :return: Execution time in seconds.
    """
    start_time = time.time()
    algorithm(*args)
    return time.time() - start_time

def generate_array_without_duplicates(size):
    """
    Generate a list of unique integers of a given size (i.e., no duplicates).

    :param size: Total size of the array.
    :return: Array with unique elements.
    """
    return random.sample(range(1, size * 10), size)

def generate_large_array(size):
    """
    Generate a large array of random integers.

    :param size: Size of the array.
    :return: A list of random integers.
    """
    return [random.randint(1, 1000) for _ in range(size)]