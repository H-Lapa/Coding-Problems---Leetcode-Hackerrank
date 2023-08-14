#https://leetcode.com/problems/sort-an-array/
#insertion sort n^2

class Solution(object):
    def sortArray(self, nums):
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j+1] < nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                j -= 1

        return nums