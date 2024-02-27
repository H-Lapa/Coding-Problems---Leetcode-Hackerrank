# using a hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):

            # checking if this new value has a combo match
            if nums[i] in hashmap:
                return [i, hashmap[nums[i]] ]
            
            #adding to the hashmap

            hashmap[target - nums[i]] = i
