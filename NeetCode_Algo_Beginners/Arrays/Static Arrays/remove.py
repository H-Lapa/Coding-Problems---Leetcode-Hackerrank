#Thought bubble
#https://leetcode.com/problems/remove-element/

#Solution 1 
# brute force, loop through and delete - using pop
#n^2

#Solution 2
#linear
# use pointers
# both at 0
# read the value, and if != val, then increment pointers, set k to value

class Solution(object):
    def removeElement(self, nums, val):

        k = 0 # write pointer

        for i in range(len(nums)):

            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k 
        