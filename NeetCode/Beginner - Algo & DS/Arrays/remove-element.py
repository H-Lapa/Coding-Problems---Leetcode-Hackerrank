# https://leetcode.com/problems/remove-element/

#first solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

#optimized solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                #current item is set to the value of the last item
                nums[i] = nums[n - 1]
                n -= 1 # reduce last item counter by 1
            else:
                i += 1
        
        return n