from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = OrderedDict()
        

    def get(self, key):
        if key in self.hashmap:
            value = self.hashmap.pop(key)
            self.hashmap[key] = value
            return value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            del self.hashmap[key]
        elif len(self.hashmap) == self.capacity:
            #remove the least recently used key
            self.hashmap.popitem(last=False)
   
        #set the key to the value 
        self.hashmap[key] = value
  


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)