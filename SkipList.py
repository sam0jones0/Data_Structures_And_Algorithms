"""Implementation of the Map data type using a SkipList."""

from random import randrange

from Stack import Stack


class SkipList:
    """A two-dimensional linked list which allows insertion and searching of key-value
    pairs in O(log(n)) time, for use in the Map data type.

    All keys must be unique and of the same comparable data type.
    """

    def __init__(self):
        self._head = None  # Entry point into the SkipList.
        self.total_data_nodes = 0
        self.len = 0

    def __len__(self):
        return self.len

    def is_empty(self):
        """Return True if SkipList is empty."""
        return self.total_data_nodes == 0

    def search(self, key):
        """Search the SkipList for a key and return the value if found, else None."""
        current = self._head

        while current:
            if current.next:
                if current.next.key == key:
                    return current.next.data
                elif current.next.key < key:
                    current = current.next
                else:
                    current = current.down
            else:
                current = current.down

        return None

    def insert(self, key, value=None):
        """Insert a key/value pair into the SkipList."""
        if self._head is None:
            # This is the first item to be added to the SkipList.
            self._head = HeaderNode()
            temp = DataNode(key, value)
            self._head.next = temp
            top = temp
            self.total_data_nodes += 1

            while flip() == 1:
                # Add another layer to the tower.
                new_head = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                new_head.down = self._head
                new_head.next = temp
                self._head = new_head
                top = temp
                self.total_data_nodes += 1
        else:
            # This is not the first item to be added to the SkipList.
            tower = Stack()
            current = self._head
            # Build a stack for the new nodes position at each level of the tower.
            while current:
                if current.next:
                    if key < current.next.key:
                        tower.push(current)
                        current = current.down
                    else:
                        current = current.next
                else:
                    tower.push(current)
                    current = current.down

            lowest_level = tower.pop()
            temp = DataNode(key, value)
            temp.next = lowest_level.next
            lowest_level.next = temp
            top = temp
            self.total_data_nodes += 1

            while flip() == 1:
                # Add the new node to its correct position on the next level up.
                if tower.is_empty():
                    new_head = HeaderNode()
                    temp = DataNode(key, value)
                    temp.down = top
                    new_head.down = self._head
                    new_head.next = temp
                    self._head = new_head
                    top = temp
                    self.total_data_nodes += 1
                else:
                    # Move up a level and insert the DataNode into its correct position.
                    next_level = tower.pop()
                    temp = DataNode(key, value)
                    temp.next = next_level.next
                    next_level.next = temp
                    temp.down = top
                    top = temp
                    self.total_data_nodes += 1
        self.len += 1

    def get_min(self):
        """Return the smallest Datanode in the Skiplist."""
        current_head = self._head
        while current_head.down:
            current_head = current_head.down
        if current_head.next:
            min_node = current_head.next
        else:
            raise ValueError("List is empty.")

        return min_node

    def pop_min(self):
        """Remove and return the smallest DataNode in the SkipList."""
        current_head = self._head
        while current_head.down:
            current_head = current_head.down
        if current_head.next:
            min_node = current_head.next
        else:
            raise ValueError("List is empty.")

        current_head = self._head
        while current_head:
            if current_head.next.key == min_node.key:
                current_head.next = current_head.next.next
                self.total_data_nodes -= 1
            current_head = current_head.down
        self._cleanup_empty_levels()

        self.len -= 1
        return min_node

    def remove(self, key):
        """Remove item with matching key."""
        tower = Stack()
        current = self._head
        # Build a stack of nodes with a next reference of key.
        while current:
            if current.next:
                if current.next.key == key:
                    tower.push(current)
                    current = current.down
                elif key > current.next.key:
                    current = current.next
                elif (
                        key.count == current.next.key.count
                        and key.level == current.next.key.level
                ):
                    current = current.next
                else:
                    current = current.down
            else:
                current = current.down
        if tower.is_empty():
            raise ValueError("Key not found.")

        while not tower.is_empty():
            current = tower.pop()
            current.next = current.next.next
            self.total_data_nodes -= 1

        self.len -= 1
        self._cleanup_empty_levels()

    def _cleanup_empty_levels(self):
        """Check if any levels are empty and remove those."""
        if not self.is_empty():
            while self._head.next is None:
                self._head = self._head.down

    def get_full_list(self):
        """Returns all the nodes (at the lowest level) as a list."""
        all_nodes = []
        current = self._head
        while current.down:
            current = current.down
        current = current.next
        while current:
            all_nodes.append((current.key, current.data))
            current = current.next

        return all_nodes


class HeaderNode:
    """A HeaderNode of a level of a SkipList. Has references to the HeaderNode below
    and to the first DataNode of its level.
    """
    def __init__(self):
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @next.setter
    def next(self, node):
        self._next = node

    @down.setter
    def down(self, node):
        self._down = node


class DataNode:
    """A DataNode of a SkipList. Holds a key and associated value. Has references
    to the next node of its level and to the node on the level below.
    """
    def __init__(self, key, value):
        self._key = key
        self._data = value
        self._next = None
        self._down = None

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @data.setter
    def data(self, value):
        self._data = value

    @next.setter
    def next(self, node):
        self._next = node

    @down.setter
    def down(self, node):
        self._down = node


def flip():
    """Simulates a coin flip, returns 0 or 1."""
    return randrange(2)


class Map:
    """A collection of key/value pairs where values can be inserted and accessed
    via their associated key.
    """
    def __init__(self):
        self.collection = SkipList()

    def __len__(self):
        return self.collection.len

    def put(self, key, value):
        """Insert a key/value pair and return nothing. Assumes key is not already present."""
        self.collection.insert(key, value)

    def get(self, key):
        """Searches for the key and returns the associated value. Requires the key
        and returns a value.
        """
        return self.collection.search(key)

    def remove(self, key):
        """Remove item with matching key."""
        return self.collection.remove(key)

    def pop_min(self):
        """Remove and return the smallest DataNode."""
        return self.collection.pop_min()
