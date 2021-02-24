from Stack import Stack


def par_checker(symbol_string):
    """Checks if number of opening and closing parenthesis match."""
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")]}":
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
        else:
            continue

    return s.is_empty()


def matches(sym_left, sym_right):
    all_left = "([{"
    all_right = ")]}"
    return all_left.index(sym_left) == all_right.index(sym_right)
