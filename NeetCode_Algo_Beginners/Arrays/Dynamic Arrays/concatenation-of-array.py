# https://leetcode.com/problems/concatenation-of-array/

#solution 1
#add arrays together using +
# solution show at the end commented, one line only

#solution 2
#create empty array of length of muns * 2
#for loop to go through nums
#assign from start and middle the new values

class Solution(object):
    def getConcatenation(self, nums):
        
        arr = [0] * (len(nums) * 2)
        s = len(nums)

        for i in range(len(nums)):
            arr[i], arr[s] = nums[i], nums[i]
            s += 1
        
        return arr
        
        #return nums + nums

        