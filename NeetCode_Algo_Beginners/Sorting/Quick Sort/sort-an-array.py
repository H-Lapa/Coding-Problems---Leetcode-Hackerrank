#quick sort

#Quick sort

class Solution(object):
    def sortArray(self, nums):
        start = 0
        end = len(nums)-1

        return self.quickSort(nums, start, end)

    def quickSort(self, nums, start, end):

        if (end-start+1 <= 1):
            return nums

        pivot = nums[end]
        left = start

        for i in range(start, end):

            if nums[i] < pivot:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        nums[end], nums[left] = nums[left], nums[end]

        self.quickSort(nums, start, left - 1)
        self.quickSort(nums, left + 1, end)

        return nums


        