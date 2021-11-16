"""Integer base converter using a stack."""


from Stack import Stack


def base_converter(decimal_num, base):
    """Returns decimal_num in the provided base."""
    rem_stack = Stack()
    chars = "0123456789ABCDEF"

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(chars[rem])
        decimal_num //= base

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string


print(base_converter(10, 16))
