"""Examples of various sequential list search functions and a comparison of
their time complexity.
"""

from timeit import Timer
import random


def sequential_search_unordered(a_list, item):
    """Iterate over each item in the list in order until item is found."""
    for pos in range(len(a_list)):
        if a_list[pos] == item:
            return True
    return False


def sequential_search_ordered(a_list, item):
    """Iterate over each item in the list in order, stopping if we find a list
    value greater than the searched item.
    """
    for pos in range(len(a_list)):
        if a_list[pos] == item:
            return True
        elif a_list[pos] > item:
            return False
    return False


def binary_search(a_list, item):
    """Binary search algorithm.

    Halves the searched list index each iteration based on whether the midpoint
    value is less/greater than the searched item.
    """
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return False


def binary_search_rec(a_list, item):
    """Recursive binary search algorithm.

    Halves the searched list on each function call based on whether the midpoint
    value is less/greater than the searched item.
    """
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint + 1 :], item)


# Create timer objects for each function and import runtime requirements.
seq_unordered = Timer(
    "sequential_search_unordered(x, random.randint(min_list, max_list))",
    "from __main__ import x, sequential_search_unordered, random, max_list, min_list",
)
seq_ordered = Timer(
    "sequential_search_ordered(x, random.randint(min_list, max_list))",
    "from __main__ import x, sequential_search_ordered, random, max_list, min_list",
)
seq_binary = Timer(
    "binary_search(x, random.randint(min_list, max_list))",
    "from __main__ import x, binary_search, random, max_list, min_list",
)
seq_binary_rec = Timer(
    "binary_search_rec(x, random.randint(min_list, max_list))",
    "from __main__ import x, binary_search_rec, random, max_list, min_list",
)

# Heading for the printed results table.
print("Average milliseconds to complete function once:")
print(f"{'n':10s}{'unordered':>15s}{'ordered':>15s}{'binary':>15s}{'binary_rec':>15s}")

# Size and iterated increment of the generated list to be searched.
min_list = 10_000
max_list = 100_001
step = min_list

for i in range(min_list, max_list, step):
    x = [random.randint(0, max_list) for j in range(i)]
    x.sort()

    # Run each timer on the same sorted list.
    unordered_t = seq_unordered.timeit(number=1000)
    ordered_t = seq_ordered.timeit(number=1000)
    binary_t = seq_binary.timeit(number=1000)
    binary_rec_t = seq_binary_rec.timeit(number=1000)

    print(
        f"{i:<10d}{ordered_t:>15.5f}{unordered_t:>15.5f}{binary_t:>15.5f}{binary_rec_t:>15.5f}"
    )
