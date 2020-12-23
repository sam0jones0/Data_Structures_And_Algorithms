"""Intro to the tree data structure using nested lists.
Improved upon in the BinaryTree.py class.
"""

def make_binary_tree(root) -> list:
    return [root, [], []]


def insert_left(root: list, new_child) -> list:
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root


def insert_right(root: list, new_child) -> list:
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


x = make_binary_tree("a")
insert_left(x, "b")
insert_right(x, "c")
insert_right(get_left_child(x), "d")
insert_left(get_right_child(x), "e")
insert_right(get_right_child(x), "f")
print(x)

