from Doubly_Linked_List_Node import Node


class DoublyLinkedList:
    """Doubly linked list implementation with items as nodes.
    Parent class for Ordered/Unordered list variants."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _add_to_empty_list(self, item):
        """Adds item if list is empty."""
        new_node = Node(item)
        self.head = new_node
        self.tail = new_node
        self.size += 1

    def _check_index_range(self, index):
        """Raise ValueError if given index out of list range."""
        if self.size <= index:
            raise ValueError("Index out of range.")

    def _remove_single_item(self):
        """Remove item from list when list size == 1"""
        self.head = None
        self.tail = None
        self.size -= 1

    def is_empty(self):
        """Returns True if list is empty."""
        return self.head is None

    def pop(self, index=None):
        """Remove and return item at given index or last item
        if no index given."""
        if index is None:
            current = self.tail
            if current.prev is None and current._next is None:
                self._remove_single_item()
                return current
            else:
                current.prev._next = None
                self.tail = current.prev
                self.size -= 1
                return current
        elif index == 0:
            current = self.head
            if current.prev is None and current._next is None:
                self._remove_single_item()
                return current
            else:
                self.head = self.head._next
                self.head.prev = None
                self.size -= 1
                return current
        else:
            current = self.find_by_index(index)
            if current != self.tail:
                current._next.prev = current.prev
            current.prev._next = current._next
            self.size -= 1
            return current

    def find_by_index(self, index):
        """Returns item at given index."""
        self._check_index_range(index)

        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current
            current = current._next
            current_index += 1

    def index(self, item):
        """Returns index of item."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current._next
            index += 1

        raise ValueError(f"'{item}' is not in the list.")

    def __str__(self):
        """Return list as string."""
        list_str = "["
        current = self.head
        while current is not None:
            list_str += str(current.data)
            if current.next is not None:
                list_str += ", "
            current = current._next
        list_str += "]"

        return list_str
