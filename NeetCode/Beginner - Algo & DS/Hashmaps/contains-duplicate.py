class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = {}
        
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = "1"

        return False
        
#using a hashmap to store the values and then check if the value is in the hashmap
#return true if it is, false if it isn't