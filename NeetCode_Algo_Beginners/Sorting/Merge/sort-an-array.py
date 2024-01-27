#merge - recursive
# very good for memory top 98% however not very good for time since creating too many arrays


class Solution(object):
    def sortArray(self, nums):

        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        arr = self.merge(self.sortArray(nums[mid:]), self.sortArray(nums[:mid]))
    
        return arr

    def merge(self, arr1, arr2):

        newArr = []

        while arr1 and arr2:
            if arr1[0] <= arr2[0]:
                newArr.append(arr1.pop(0))
            else:
                newArr.append(arr2.pop(0))
                
        if not arr1:
            newArr += arr2

        if not arr2:
            newArr += arr1

        return newArr
        
        