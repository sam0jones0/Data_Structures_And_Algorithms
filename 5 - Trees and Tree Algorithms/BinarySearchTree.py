class BinarySearchTree:
    """Binary Search Tree implementation with TreeNode nodes."""

    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return bool(self._get(key, self.root))

    def __delitem__(self, key):
        self.delete(key)

    def put(self, key, value):
        """Add item to the Binary Search Tree."""
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._put(key, value, self.root)
        self.size += 1

    def _put(self, key, value, current_node):
        """Recursively search tree for position of new node."""
        if key < current_node.key:
            if current_node.left_child:
                # There is a left child, recursively search it.
                self._put(key, value, current_node.left_child)
            else:
                # No child; found position for new node.
                current_node.left_child = TreeNode(key, value, parent=current_node)
        else:
            if current_node.right_child:
                # There is a right child, recursively search it.
                self._put(key, value, current_node.right_child)
            else:
                # No child; found position for new node.
                current_node.right_child = TreeNode(key, value, parent=current_node)

    def get(self, key):
        """Search for key and return value."""
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None

    def _get(self, key, current_node):
        """Helper function to recursively search tree for key."""
        if not current_node:
            return None
        if current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        """Delete TreeNode with matching key."""
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Key not found in tree.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Key not found in tree.")

    def _delete(self, node_to_remove):
        """Helper method to delete node while retaining Tree structure."""
        if node_to_remove.is_leaf():  # Removing a node with no children.
            # Only need to update parent's references.
            if node_to_remove.is_left_child():
                node_to_remove.parent.left_child = None
            else:
                node_to_remove.parent.right_child = None

        elif node_to_remove.has_children():  # Removing a node with two children.
            successor = node_to_remove.find_successor()
            successor.splice_out()
            node_to_remove.key = successor.key
            node_to_remove.value = successor.value

        else:  # Removing a node with one child; update parent and child references.
            if node_to_remove.left_child:
                if node_to_remove.is_left_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.left_child
                elif node_to_remove.is_right_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.left_child
                else:
                    node_to_remove.replace_value(
                        node_to_remove.left_child.key,
                        node_to_remove.left_child.value,
                        node_to_remove.left_child.left_child,
                        node_to_remove.left_child.right_child,
                    )
            else:
                if node_to_remove.is_left_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.right_child
                elif node_to_remove.is_right_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                else:
                    node_to_remove.replace_value(
                        node_to_remove.right_child.key,
                        node_to_remove.right_child.value,
                        node_to_remove.right_child.left_child,
                        node_to_remove.right_child.right_child,
                    )


class TreeNode:
    """Tree node of a Binary Search Tree."""

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.left_child:
                yield from self.left_child
            yield self.key
            if self.right_child:
                yield from self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_a_child(self):
        return self.left_child or self.right_child

    def has_children(self):
        return self.left_child and self.right_child

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def find_successor(self):
        successor = None
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_a_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent
