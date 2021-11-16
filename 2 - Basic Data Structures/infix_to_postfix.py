from Stack import Stack


def infix_to_postfix(expression):
    """Translates given infix expression to postfix."""
    prec = {"**": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    op_stack = Stack()
    output_list = []
    input_list = expression.split()

    for token in input_list:
        if token not in ["*", "/", "+", "-", "(", ")", "**"]:
            output_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                output_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and prec[op_stack.peek()] >= prec[token]:
                output_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        output_list.append(op_stack.pop())

    return " ".join(output_list)


def eval_postfix(expression):
    """Evaluates given postfix expression."""
    eval_stack = Stack()
    input_list = expression.split()
    try:
        for token in input_list:
            if represents_int(token):
                eval_stack.push(int(token))
            else:
                first_recent = eval_stack.pop()
                second_recent = eval_stack.pop()
                eval_stack.push(eval(f"{second_recent}{token}{first_recent}"))
    except IndexError as error:
        print(f"Operands must be int: '{error}'")

    return eval_stack.pop()


def represents_int(s):
    """Helper function to check whether given parameter is an int."""
    try:
        int(s)
        return True
    except ValueError:
        return False


expression = "5 * 3 ** ( 4 - 2 )"
# as_postfix = infix_to_postfix(expression)
# print(f"{expression} in postfix: {as_postfix} = {eval_postfix(as_postfix)}")

print(infix_to_postfix(expression))

# print(eval_postfix("17 10 + 3 * 9 /"))
