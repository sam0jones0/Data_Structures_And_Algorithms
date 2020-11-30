class Node:
    """A node of a linked list."""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None
        self._prev = None

    @property
    def data(self):
        """Get node data."""
        return self._data

    @data.setter
    def data(self, node_data):
        """Set node data."""
        self._data = node_data

    @property
    def next(self):
        """Get next node."""
        return self._next

    @next.setter
    def next(self, node_next):
        """Set next node."""
        self._next = node_next

    @property
    def prev(self):
        """Get previous node."""
        return self._prev

    @prev.setter
    def prev(self, node_prev):
        """Set previous node."""
        self._prev = node_prev

    def __str__(self):
        """String."""
        return str(self._data)


class UnorderedList:
    """Unordered doubly linked list implementation with items as nodes."""

    def __init__(self):
        self.head = None
        self.tail = None

    def _add_to_empty_list(self, item):
        """Adds item if list is empty."""
        new_node = Node(item)
        self.head = new_node
        self.tail = new_node

    def _check_index_range(self, index):
        """Raise ValueError if given index out of list range."""
        if self.size() <= index:
            raise ValueError("Index out of range.")

    def is_empty(self):
        """Returns True if list is empty."""
        return self.head is None

    def size(self):
        """Returns size of list as int."""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def add(self, item):
        """Add item to list."""
        if self.is_empty():
            self._add_to_empty_list(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, item):
        """Append item onto the end of the list."""
        if self.is_empty():
            self._add_to_empty_list(item)
        else:
            new_node = Node(item)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, item, index):
        """Insert item into list at index."""
        current = self.find_by_index(index)
        new_node = Node(item)
        new_node.next = current
        new_node.prev = current.prev

        if current.prev is None:
            self.head = new_node

        current.prev.next = new_node
        current.prev = new_node

    def pop(self, index=None):
        """Remove and return item at given index or last item
           if no index given."""
        if index is None:
            current = self.tail
            current.prev.next = None
            self.tail = current.prev
            return current
        elif index == 0:
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            return current
        else:
            current = self.find_by_index(index)
            if current != self.tail:
                current.next.prev = current.prev
            current.prev.next = current.next

            return current

    def search(self, item):
        """Returns True if item is in list."""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def find_by_index(self, index):
        """Returns item at given index."""
        self._check_index_range(index)

        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current
            current = current.next
            current_index += 1

    def index(self, item):
        """Returns index of item."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1

        raise ValueError(f"'{item}' is not in the list.")

    def remove(self, item):
        """Remove item from the list."""
        current = self.head
        while current is not None:
            if current.data == item:
                break
            current = current.next

        if current is None:
            raise ValueError(f"{item} not in list.")
        elif current.prev is None:
            self.head = current.next
            self.head.prev = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def __str__(self):
        """Return list as string."""
        list_str = '['
        current = self.head
        while current is not None:
            list_str += str(current.data)
            if current.next is not None:
                list_str += ', '
            current = current.next
        list_str += ']'

        return list_str
