from timeit import Timer
import random


def sequential_search_unordered(a_list, item):
    for pos in range(len(a_list)):
        if a_list[pos] == item:
            return True
    return False


def sequential_search_ordered(a_list, item):
    for pos in range(len(a_list)):
        if a_list[pos] == item:
            return True
        elif a_list[pos] > item:
            return False
    return False


def binary_search(a_list, item):
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


seq_unordered = Timer("sequential_search_unordered(x, random.randint(min_list, max_list))",
                      "from __main__ import x, sequential_search_unordered, random, max_list, min_list")
seq_ordered = Timer("sequential_search_ordered(x, random.randint(min_list, max_list))",
                    "from __main__ import x, sequential_search_ordered, random, max_list, min_list")
seq_binary = Timer("binary_search(x, random.randint(min_list, max_list))",
                   "from __main__ import x, binary_search, random, max_list, min_list")

print(f"{'n':10s}{'unordered':>15s}{'ordered':>15s}{'binary':>15s}")

min_list = 10_000
max_list = 100_001
step = min_list

for i in range(min_list, max_list, step):
    x = [random.randint(0, max_list) for j in range(i)]
    x.sort()
    unordered_t = seq_unordered.timeit(number=1000)
    ordered_t = seq_ordered.timeit(number=1000)
    binary_t = seq_binary.timeit(number=1000)
    print(f"{i:<10d}{ordered_t:>15.5f}{unordered_t:>15.5f}{binary_t:>15.5f}")
