import operator

from BinaryTree import BinaryTree
from Stack import Stack


def build_parse_tree(expr):
    """Parse representation of a math expression (int only) to tree.
    E.g. '( ( 10 + 5 ) * 3 )'
    """
    fp_list = expr.split()
    # Stack is used to keep track of parent nodes.
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == "(":
            # Add a new node as left child of current node,
            # and descend to the left child.
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child

        elif i in ["+", "-", "*", "/"]:
            # Set current node root value to operator and add new node as right
            # child of current node, then descend to right child.
            current_tree.key = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child

        elif i == ")":
            # Go to parent of current node.
            current_tree = p_stack.pop()

        elif i not in ["+", "-", "*", "/", ")"]:
            try:
                # Set current node root value to the number and return to parent.
                current_tree.key = int(i)
                current_tree = p_stack.pop()

            except ValueError:
                raise ValueError(f"Token '{i}' is not a valid integer.")

    return expr_tree


def evaluate(parse_tree: BinaryTree):
    """Evaluate math expression tree and return int result."""
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        # Apply operator to results from recursive eval of left and right children.
        return operators[parse_tree.key](evaluate(left_child), evaluate(right_child))
    else:
        # Base case; this is a leaf node as both children are None.
        return parse_tree.key


def postorder_eval(parse_tree: BinaryTree):
    """Evaluate math expression tree and return int result via
    postorder traversal.
    """
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result_1 = None
    result_2 = None
    if parse_tree:
        result_1 = postorder_eval(parse_tree.get_left_child())
        result_2 = postorder_eval(parse_tree.get_right_child())
        if result_1 and result_2:
            return operators[parse_tree.get_root_val()](result_1, result_2)
        else:
            return parse_tree.get_root_val()


# pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
# print(postorder_eval(pt))
