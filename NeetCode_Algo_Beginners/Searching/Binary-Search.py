# first attempt using slicing

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pos = 0

        while len(nums) > 1:

            mid = len(nums) // 2

            if nums[mid] == target:
                return pos + mid

            if nums[mid] > target:
                nums = nums[:mid]
            else:
                nums = nums[mid:]
                pos += mid

        if len(nums) < 1 or nums[0] != target:
            return -1

        return pos


#using pointers

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid + 1
            else:
                start = mid

        if len(nums) < 1 or nums[mid] != target:
            return -1

        return mid
