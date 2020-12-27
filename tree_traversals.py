"""Various tree traversal algorithms. Note that these all work
on tree types other than BinaryTree.
"""

from parse_tree import *


def preorder(tree: BinaryTree):
    """Preorder tree traversal."""
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree: BinaryTree):
    """Postorder tree traversal."""
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def inorder(tree: BinaryTree):
    """Inorder tree traversal."""
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


def print_exp(tree: BinaryTree):
    """Inorder tree traversal to print original math expression."""
    result = ""
    if tree:
        result = "(" + print_exp(tree.get_left_child())
        result = result + str(tree.get_root_val())
        result = result + print_exp(tree.get_right_child()) + ")"
    return result


pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
inorder(pt)
print(print_exp(pt))