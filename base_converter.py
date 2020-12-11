"""Integer base converter using a stack."""


from Stack import Stack


def base_converter(decimal_num, base):
    """Returns decimal_num in the provided base."""
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num //= base

    bin_string = ''
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string
