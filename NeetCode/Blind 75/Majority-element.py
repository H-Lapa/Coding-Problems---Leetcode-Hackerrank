class Solution(object):
    def majorityElement(self, nums):
        val = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == val:
                count += 1
            elif nums[i] != val and count == 0:
                val = nums[i]
            else:
                count -= 1

        return val
