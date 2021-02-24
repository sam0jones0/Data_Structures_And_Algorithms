class Stack:
    """Stack implementation as a list."""

    def __init__(self):
        """Create new stack."""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return an item from the top of the stack."""
        return self._items.pop()

    def peek(self):
        """Return an item from the top of the stack without removing it."""
        try:
            return self._items[-1]
        except IndexError as error:
            print(f"Stack might be empty: {error}")
            return None

    def size(self):
        """Return the size (int) of the stack."""
        return len(self._items)
