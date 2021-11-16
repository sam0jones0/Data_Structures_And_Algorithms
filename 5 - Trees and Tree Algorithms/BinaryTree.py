class BinaryTree:
    """Simple binary tree."""

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """Insert left child node to current node."""
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        """Insert right child node to current node."""
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

    def get_root_val(self):
        """Return root value of current node."""
        return self.key

    def set_root_val(self, new_obj):
        """Set root value of current node."""
        self.key = new_obj

    def get_left_child(self):
        """Return left child node of current node"""
        return self.left_child

    def get_right_child(self):
        """Return right child node of current node"""
        return self.right_child
