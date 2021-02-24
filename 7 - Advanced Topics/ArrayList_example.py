"""An exploration of the principles behind Python's list implementation, demonstrating
some key ideas of the Array (C, C++ / Java) data type. There is no practical use for
this whatsoever.
"""


class ArrayList:
    """A data structure similar in design to Python's list implementation. Using key
    elements from the Array (C, C++ / Java) data type.
    """
    def __init__(self):
        self.size_exponent = 0
        self.max_size = 0
        self.last_index = 0
        self.my_array = []

    def append(self, val):
        """Append value to end of array."""
        if self.last_index > self.max_size - 1:
            self.__resize()
        self.my_array[self.last_index] = val
        self.last_index += 1

    def __resize(self):
        """Calculate new size for the array using 2**size_exponent. Automatically
        called when the current array is full.
        """
        new_size = 2 ** self.size_exponent
        print(f"New size = {new_size}")
        new_array = [0] * new_size
        for index in range(self.max_size):
            new_array[index] = self.my_array[index]
        self.max_size = new_size
        self.my_array = new_array
        self.size_exponent += 1

    def insert(self, index, value):
        """Insert value at index, shifting all other values to the right."""
        if self.last_index > self.max_size - 1:
            self.__resize()
        for i in range(self.last_index, index - 1, -1):
            self.my_array[i + 1] = self.my_array[i]
        self.last_index += 1
        self.my_array[index] = value

    def pop(self, index=None):
        """Remove and return value at index, or from the end of the array if no index
        is provided. Shifts all other values to the left.
        """
        if index is None:
            index = self.last_index - 1
        result = self.my_array[index]
        self.__del(index)
        return result

    def __del(self, index):
        """Delete value at index. Shifts all other values to the left."""
        if index < self.last_index:
            for i in range(index, self.last_index - 1):
                self.my_array[i] = self.my_array[i + 1]
            # Manually remove last item in array to avoid resizing a full list.
            self.my_array[self.last_index - 1] = 0
            self.last_index -= 1
        else:
            raise LookupError("Index out of bounds.")

    def __index__(self, value):
        """Return index int of provided value."""
        for index in range(0, self.last_index + 1):
            if self.my_array[index] == value:
                return index
        raise LookupError("No index for value found.")

    def __iter__(self):
        """Generate iterator object."""
        self.n = 0
        return self

    def __next__(self):
        """Step through iterator object."""
        if self.n < self.last_index:
            result = self.my_array[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        """Return value at index."""
        if index < self.last_index:
            return self.my_array[index]
        else:
            raise LookupError("Index out of bounds.")

    def __setitem__(self, index, value):
        """Set value at index."""
        if index < self.last_index:
            self.my_array[index] = value
        else:
            raise LookupError("Index out of bounds.")
