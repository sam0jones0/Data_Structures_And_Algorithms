"""Example of a simple integer hashing algorithm using modulo of table size."""


def hash_int(an_int, table_size, hash_table):
    """Simple hash table resolving collisions with linear probing."""
    hash_index = an_int % table_size
    if not hash_table[hash_index]:
        # The desired table position is empty.
        hash_table[hash_index] = an_int
    else:
        # Linear probe for next available hash position.
        original_hash_index = hash_index
        while True:
            hash_index += 1
            if hash_index > table_size - 1:
                hash_index = 0
            if hash_index == original_hash_index:
                raise IndexError("Hash table is full.")
            if not hash_table[hash_index]:
                hash_table[hash_index] = an_int
                return


def make_hash_table(table_size):
    """Make empty hash table."""
    return [None] * table_size


my_table_size = 11
my_hash_table = make_hash_table(my_table_size)
my_ints = [113, 117, 97, 100, 114, 108, 116, 105, 99]

for my_int in my_ints:
    hash_int(my_int, my_table_size, my_hash_table)

print(my_hash_table)
