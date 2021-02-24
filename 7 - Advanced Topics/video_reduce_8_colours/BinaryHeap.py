class BinaryHeapOT:
    """Heap implementation using a balanced binary tree represented as
    a single list.
    """
    def __init__(self):
        self._heap = []

    def _perc_up(self, cur_idx):
        """Percolate a new item up to its proper position, restoring the
        heap structure/order properties.
        """
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx]
                )
            cur_idx = parent_idx

    def _perc_down(self, cur_idx):
        """Percolate a new item down to its proper position, restoring the
        heap structure/order properties.
        """
        while (cur_idx * 2) + 1 < len(self._heap):
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx]
                )
            else:
                return
            cur_idx = min_child_idx

    def _get_min_child(self, parent_idx):
        """Return index of parent's smallest child."""
        if (parent_idx * 2) + 2 > len(self._heap) - 1:
            # Parent only has one child, return it.
            return (parent_idx * 2) + 1
        if self._heap[(parent_idx * 2) + 1] < self._heap[(parent_idx * 2) + 2]:
            # Left child is smaller.
            return (parent_idx * 2) + 1
        # Right child is smaller.
        return (parent_idx * 2) + 2

    def heapify(self, not_a_heap):
        """Build a heap from a list of keys."""
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx -= 1

    def insert(self, item):
        """Insert item into heap."""
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def delete(self):
        """Delete and return item at min position."""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def is_empty(self):
        return not bool(self._heap)

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)
