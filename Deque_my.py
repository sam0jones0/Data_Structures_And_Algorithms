class Deque:
    """Deque implementation as a list."""

    def __init__(self):
        """Create a new deque."""
        self._items = []

    def is_empty(self):
        """Check if deque is empty."""
        return not bool(self._items)

    def add_front(self, item):
        """Add item to front of deque."""
        self._items.append(item)

    def add_rear(self, item):
        """Add item to rear of deque."""
        self._items.insert(0, item)

    def remove_front(self):
        """Remove and return item from front of deque."""
        return self._items.pop()

    def remove_rear(self):
        """Remove and return item from rear of deque."""
        return self._items.pop(0)

    def size(self):
        """Return size of deque as int."""
        return len(self._items)
