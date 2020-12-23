"""Various number sorting algorithms."""

import random
from timeit import Timer


def bubble_sort(my_list):
    """Sorts list from smallest to largest ascending using bubble sort."""
    for i in range(len(my_list) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            a, b = my_list[j], my_list[j + 1]
            if a > b:
                my_list[j], my_list[j + 1] = b, a
                exchanges = True
        if not exchanges:
            break


def selection_sort(my_list):
    """Sorts list from smallest to largest ascending using selection sort."""
    for i in range(len(my_list) - 1, 0, -1):
        lrg_value, lrg_index = my_list[0], 0
        for j in range(i):
            if my_list[j + 1] > lrg_value:
                lrg_value, lrg_index = my_list[j + 1], j + 1
        my_list[i], my_list[lrg_index] = my_list[lrg_index], my_list[i]


def insertion_sort(my_list):
    """Sorts list from smallest to largest ascending using insertion sort."""
    for i in range(1, len(my_list)):
        cur_val = my_list[i]
        cur_pos = i

        while cur_pos > 0 and my_list[cur_pos - 1] > cur_val:
            my_list[cur_pos] = my_list[cur_pos - 1]
            cur_pos -= 1
        my_list[cur_pos] = cur_val


def shell_sort(my_list):
    """Sorts list from smallest to largest ascending using shell sort sort."""
    sublist_count = len(my_list) // 2
    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(my_list, start_pos, sublist_count)
        sublist_count //= 2


def gap_insertion_sort(my_list, start, gap):
    """Should only be called from within shell_sort"""
    for i in range(start + gap, len(my_list), gap):
        cur_val = my_list[i]
        cur_pos = i

        while cur_pos >= gap and my_list[cur_pos - gap] > cur_val:
            my_list[cur_pos] = my_list[cur_pos - gap]
            cur_pos -= gap
        my_list[cur_pos] = cur_val


def merge_sort_slice(my_list):
    """Sorts list from smallest to largest ascending using recursive merge sort,
    with slicing.
    """
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort_slice(left_half)
        merge_sort_slice(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                # Add the smaller left half item
                my_list[k] = left_half[i]
                i += 1
            else:
                # Add the smaller right half item
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            # Add any leftover from left half
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            # Add any leftover from right half.
            my_list[k] = right_half[j]
            j += 1
            k += 1


def merge_sort(my_list, start, end):
    """Sorts list from smallest to largest ascending using recursive merge sort,
    without slicing.
    """
    if end - start > 1:
        mid = (start + end) // 2

        merge_sort(my_list, start, mid)  # Left half.
        merge_sort(my_list, mid, end)  # Right half.

        i, j = start, mid
        merged = []
        while i < mid and j < end:
            if my_list[i] <= my_list[j]:
                merged.append(my_list[i])
                i += 1
            else:
                merged.append(my_list[j])
                j += 1

        # Add in unmerged from left half to temp list.
        merged.extend(my_list[i:mid])
        # Inject merged list (which doesn't include unmerged from right half) into main list.
        my_list[start:start + len(merged)] = merged


def quick_sort(my_list):
    """Sorts list from smallest to largest ascending using recursive quicksort"""
    quick_sort_helper(my_list, 0, len(my_list) - 1)


def quick_sort_helper(my_list, first, last):
    """Recursively calls the partition function on on each half of the split list."""
    if first < last:
        split = partition(my_list, first, last)
        quick_sort_helper(my_list, first, split - 1)
        quick_sort_helper(my_list, split + 1, last)


def partition(my_list, first, last):
    """One pass of the quicksort function. Locates the split point and sorts
    accordingly.
    """
    pivot_val = my_list[first]  # We are testing with random lists so first can be used as pivot.
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and my_list[left_mark] <= pivot_val:
            left_mark += 1
        while left_mark <= right_mark and my_list[right_mark] >= pivot_val:
            right_mark -= 1
        if right_mark < left_mark:
            # Split point found.
            done = True
        else:
            # Swap values at left and right mark.
            my_list[left_mark], my_list[right_mark] = (
                my_list[right_mark],
                my_list[left_mark]
            )
    # Swap right mark (split point) to first position (pivot point).
    my_list[first], my_list[right_mark] = my_list[right_mark], my_list[first]

    return right_mark


# Create timer objects for each function and import runtime requirements.
bubble = Timer("bubble_sort(x[:])", "from __main__ import bubble_sort, x")
selection = Timer("selection_sort(x[:])", "from __main__ import selection_sort, x")
insertion = Timer("insertion_sort(x[:])", "from __main__ import insertion_sort, x")
shell = Timer("shell_sort(x[:])", "from __main__ import shell_sort, gap_insertion_sort, x")
merge_s = Timer("merge_sort_slice(x[:])", "from __main__ import merge_sort_slice, x")
merge = Timer("merge_sort(x[:], 0, len(x))", "from __main__ import merge_sort, x")
quick = Timer("quick_sort(x[:])", "from __main__ import quick_sort,"
                                  "quick_sort_helper, partition, x")

# Heading for the printed results table.
print("Average milliseconds to complete sort function once:")
print(f"{'n':10s}{'bubble':>15s}{'selection':>15s}{'insertion':>15s}"
      f"{'shell':>15s}{'merge_s':>15s}{'merge':>15s}{'quick':>15s}")

for i in range(100, 1_001, 100):
    x = [random.randint(1, 10_001) for j in range(i)]

    # Run each timer on the same random list.
    bubble_t = bubble.timeit(number=100)
    selection_t = selection.timeit(number=100)
    insertion_t = insertion.timeit(number=100)
    shell_t = shell.timeit(number=100)
    merge_s_t = merge_s.timeit(number=100)
    merge_t = merge.timeit(number=100)
    quick_t = quick.timeit(number=100)

    # Print a line of the results table.
    print(f"{i:<10d}{bubble_t * 10:>15.5f}{selection_t * 10:>15.5f}{insertion_t * 10:>15.5f}"
          f"{shell_t * 10:>15.5f}{merge_s_t * 10:>15.5f}{merge_t * 10:>15.5f}{quick_t * 10:>15.5f}")
