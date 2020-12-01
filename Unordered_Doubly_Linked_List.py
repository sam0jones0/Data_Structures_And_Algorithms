from Doubly_Linked_List_Node import Node
from Doubly_Linked_List import DoublyLinkedList


class UnorderedList(DoublyLinkedList):
    """Unordered doubly linked list implementation with items as nodes."""

    def __init__(self):
        super().__init__()

    def add(self, item):
        """Add item to list."""
        if self.is_empty():
            self._add_to_empty_list(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def append(self, item):
        """Append item onto the end of the list."""
        if self.is_empty():
            self._add_to_empty_list(item)
        else:
            new_node = Node(item)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1

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
        self.size += 1

    def search(self, item):
        """Returns True if item is in list."""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        """Remove item from the list."""
        current = self.head
        while current is not None:
            if current.data == item:
                break
            current = current.next

        if current is None:
            raise ValueError(f"{item} not in list.")
        elif current.prev is None and current.next is None:
            self._remove_single_item()
        elif current.prev is None:
            self.head = current.next
            self.head.prev = None
            self.size -= 1
        elif current.next is None:
            current.prev.next = None
            self.tail = current.prev
            self.size -= 1
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
