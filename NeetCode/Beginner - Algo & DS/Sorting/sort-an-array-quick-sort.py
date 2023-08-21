class Solution(object):
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, low, high):
        if low < high:
            pivot_index = self.partition(nums, low, high)
            self.quicksort(nums, low, pivot_index - 1)
            self.quicksort(nums, pivot_index + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[high]  # Using Lomuto's partitioning scheme
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
