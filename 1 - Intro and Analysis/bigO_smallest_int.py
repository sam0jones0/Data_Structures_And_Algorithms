"""Some methods of finding the smallest number in a list compared for
time complexity.
"""

import time
import random


def get_min_number_slow(some_list):
    """Slow function to return smallest number in a given list."""
    current_smallest = some_list[0]
    for i in some_list:
        is_smallest = True
        for j in some_list:
            if i > j:
                is_smallest = False
        if is_smallest:
            current_smallest = i

    return current_smallest


def get_min_number_fast(some_list):
    """Fast function to return smallest number in a given list."""
    return min(some_list)


def return_times(func):
    """Times execution of a get_min_number function on a large random list."""
    times = []
    for list_size in range(1_000, 10_001, 1_000):
        a_list = [random.randrange(100_000_000) for x in range(list_size)]
        start = time.time()
        min_number = func(a_list)
        end = time.time()
        times.append(end - start)
        print(f"Min: {min_number}. List size {str(list_size)}. Time: {str(end - start)}")
    return times


slow_times = return_times(get_min_number_slow)
fast_times = return_times(get_min_number_fast)

for i in range(0, len(slow_times)):
    print(f"Time difference between func: {slow_times[i] - fast_times[i]}")
