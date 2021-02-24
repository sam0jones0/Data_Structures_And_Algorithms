class HashTable:
    """Hash table using two parallel lists (key/value) to implement the map
     abstract data type.
     """
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """Add key/data to map."""
        hash_value = self.hash_function(key, len(self.slots))

        if self.slot_empty(hash_value):
            # This slot is empty and can be used.
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                # Replace data at existing key.
                self.data[hash_value] = data
            else:
                # Probe for next available slot.
                next_slot = self.rehash(hash_value, len(self.slots))
                while (
                    # Find the first empty slot or slot with an existing key.
                    not self.slot_empty(next_slot)
                    and self.slots[next_slot] != key
                ):
                    if next_slot == hash_value:
                        # Each slot has been probed.
                        raise ValueError("No free slots.")
                    else:
                        next_slot = self.rehash(next_slot, len(self.slots))

                if self.slot_empty(next_slot):
                    # Found next available slot.
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    # Linear probe found an existing key.
                    self.data[next_slot] = data

    def get(self, key):
        """Returns data at slot key."""
        start_slot = self.hash_function(key, len(self.slots))

        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    # Each slot has been probed.
                    return None

    def delete(self, key):
        """Delete key/data pair."""
        start_slot = self.hash_function(key, len(self.slots))

        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                self.slots[position] = 'DEL'
                self.data[position] = None
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    # Each slot has been probed.
                    return None

    def hash_function(self, key, size):
        """Return hash value."""
        return key % size

    def rehash(self, old_hash, size):
        """Rehash with 'plus 1' linear probe."""
        return (old_hash + 1) % size

    def slot_empty(self, hash_value):
        """Returns True if slot is open for insertion, False otherwise.
        Previously occupied slots which have been deleted are considered open.
        """
        if self.slots[hash_value] is None or self.slots[hash_value] == 'DEL':
            return True
        else:
            return False

    def __len__(self):
        return len(self.slots)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        return self.delete(key)
