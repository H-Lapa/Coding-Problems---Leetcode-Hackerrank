# [4, 3, 2, 1]

# [3, 4, 2, 1]

# [2, 3, 4, 1]

#insertion sort

class Solution(object):
    def sortArray(self, nums):
        
        for i in range(1, len(nums)):

            key = nums[i]

            j = i - 1

            while j >= 0 and key < nums[j]:

                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = key

        return nums
        