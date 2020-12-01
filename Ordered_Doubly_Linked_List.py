from Doubly_Linked_List_Node import Node
from Doubly_Linked_List import DoublyLinkedList


class OrderedList(DoublyLinkedList):
    """Ordered (ascending) doubly linked list implementation with items as nodes."""

    def __init__(self):
        super().__init__()

    def add(self, item):
        """Add item to list preserving ascending order."""
        if self.is_empty():
            self._add_to_empty_list(item)
        else:
            current = self.head
            new_node = Node(item)

            while current is not None and current.data < item:
                current = current.next

            if current is None:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
                self.size += 1
            elif current is self.head:
                self.head = new_node
                new_node.next = current
                new_node.prev = current.prev
                current.prev = new_node
                self.size += 1
            else:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
                self.size += 1

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
            self.size -= 1
        elif current.next is None:
            current.prev.next = None
            self.tail = current.prev
            self.size -= 1
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
