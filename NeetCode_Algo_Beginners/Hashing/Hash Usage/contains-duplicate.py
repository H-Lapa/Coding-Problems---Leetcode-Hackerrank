class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}

        # for every number in the array
        for num in nums:

            #check if the number exists in the hashmap
            if num in hashmap:
                #It already exists, it means this new one is a duplicate
                return True
            else:
                #doesn't exists yet in hashmap so add it
                hashmap[num] = 1


        return False