#,my initial approach was to use a hashmap and a queue to keep track of the least recently used element

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hashmap = {}
        self.keyTracker = []

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.keyTracker.remove(key)
            self.keyTracker.append(key)
            return self.hashmap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            self.hashmap[key] = value
            self.keyTracker.remove(key)
            self.keyTracker.append(key)
        else:
            if len(self.hashmap) >= self.size:
                del self.hashmap[self.keyTracker.pop(0)]
            
            # Add to the hashmap and key tracker
            self.hashmap[key] = value 
            self.keyTracker.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# now I will be using an ordered Dict to solve the problem

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                #Pop the first item (least recently used)
                self.cache.popitem(last=False)
            
        # Add to the hashmap and key tracker
        self.cache[key] = value 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)