class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.set = [None] * self.capacity
        
    def add(self, key: int) -> None:
        if self.size / self.capacity >= 0.75:  # Check load factor - if over 75% full then resize
            self.resize(self.capacity * 2)
        
        #finding the index through hashing
        index = hash(key) % self.capacity

        #if there is no conflict
        if self.set[index] is None:
            self.set[index] = [key]
        else:
            # if there is already an item in the location
            if key not in self.set[index]:
                #each location stores an array - which stores many keys
                self.set[index].append(key) # key is being appended to that array

        #updating size
        self.size += 1

    def remove(self, key: int) -> None:
        index = hash(key) % self.capacity

        if self.set[index] is not None:
            try:
                self.set[index].remove(key)
                self.size -= 1
                if not self.set[index]:  # If the list at index is empty, set it to None
                    self.set[index] = None
            except ValueError:
                pass  # Key was not found, do nothing

    def contains(self, key: int) -> bool:
        index = hash(key) % self.capacity
        if self.set[index] is None:
            return False
        return key in self.set[index]

    def resize(self, new_capacity):
        new_set = [None] * new_capacity
        old_set = self.set
        self.set = new_set
        self.capacity = new_capacity
        self.size = 0  # Reset size to correctly add elements back
        for bucket in old_set:
            if bucket is not None:
                for key in bucket:
                    self.add(key)  # Rehash all keys
