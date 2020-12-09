from Stack import Stack


# Base converter implemented recursively.
def to_str_recursive(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str_recursive(n // base, base) + convert_string[n % base]


# Base converter implemented using a stack.
def to_str_stack(n, base):
    r_stack = Stack()
    convert_string = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res += r_stack.pop()
    return res


# Removes non-alpha characters from a string.
def remove_white(s):
    return ''.join([char.lower() for char in s if char.isalpha()])


# Checks if a given string (removing whitespace) is a palindrome.
def is_pal(s):
    s = remove_white(s)
    if len(s) < 2:
        return True
    else:
        if s[0] != s[-1]:
            return False
    return is_pal(s[1:-1])

