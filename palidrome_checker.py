from Deque_my import Deque


def palindrome_checker(test_string):
    """Returns True if test_string is a palindrome."""
    d = Deque()
    for char in test_string:
        d.add_front(char.lower())

    while d.size() > 1:
        if d.remove_rear() != d.remove_front():
            return False

    return True


print(palindrome_checker("Able was I ere I saw Elba"))
