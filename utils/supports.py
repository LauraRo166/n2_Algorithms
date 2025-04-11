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

def generate_array_with_duplicates(size, duplication_factor=0.1):
    """
    Generate a list of integers of a given size with some duplicates.

    :param size: Total size of the array.
    :param duplication_factor: Fraction of elements that will be duplicates.
    :return: Array with intentional duplicates.
    """
    base_size = int(size * (1 - duplication_factor))
    base_elements = [random.randint(1, 1000) for _ in range(base_size)]
    duplicates = random.choices(base_elements, k=size - base_size)
    return base_elements + duplicates

def generate_large_array(size):
    """
    Generate a large array of random integers.

    :param size: Size of the array.
    :return: A list of random integers.
    """
    return [random.randint(1, 1000) for _ in range(size)]