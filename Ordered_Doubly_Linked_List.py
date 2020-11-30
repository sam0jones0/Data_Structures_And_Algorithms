from Doubly_Linked_List_Node import Node


class OrderedList:
    """Ordered (ascending) doubly linked list implementation with items as nodes."""

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

    def _remove_single_item(self):
        """Remove item from list when list size == 1"""
        self.head = None
        self.tail = None

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
        """Add item to list preserving ascending order."""
        if self.is_empty():
            self._add_to_empty_list(item)
        else:
            current = self.head
            new_node = Node(item)

            while current.next is not None and current.data < item:
                current = current.next

            if current.next is None:
                new_node.prev = current
                current.next = new_node
                self.tail = new_node
            elif current is self.head:
                self.head = new_node
                new_node.next = current
                new_node.prev = current.prev
                current.prev = new_node
            else:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node

    def pop(self, index=None):
        """Remove and return item at given index or last item
           if no index given."""
        if index is None:
            current = self.tail
            if current.prev is None and current.next is None:
                self._remove_single_item()
                return current
            else:
                current.prev.next = None
                self.tail = current.prev
                return current
        elif index == 0:
            current = self.head
            if current.prev is None and current.next is None:
                self._remove_single_item()
                return current
            else:
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
            if current.data > item:
                return False
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
            if current.data > item:
                raise ValueError(f"{item} not in list.")
            current = current.next

        if current is None:
            raise ValueError(f"{item} not in list.")
        elif current.prev is None and current.next is None:
            self._remove_single_item()
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
