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
        
        
# Now the solution using pointers

#merge - recursive

class Solution(object):
    def sortArray(self, nums, start=0, end=None):
        if end is None:
            end = len(nums)

        if end - start > 1:  # More than one element
            mid = (start + end) // 2
            self.sortArray(nums, start, mid)  # Sort the first half
            self.sortArray(nums, mid, end)    # Sort the second half
            self.merge(nums, start, mid, end) # Merge the sorted halves

        return nums

        
    def merge(self, nums, start, mid, end):

        arr1 = nums[start:mid]
        arr2 = nums[mid:end]
        newArr = []

        while arr1 and arr2:
            if arr1[0] <= arr2[0]:
                newArr.append(arr1.pop(0))
            else:
                newArr.append(arr2.pop(0))
                
        if not arr1 and arr2:
            newArr += arr2

        if not arr2 and arr1:
            newArr += arr1

        # Copy the elements of newArr back into nums
        for i in range(len(newArr)):
            nums[start + i] = newArr[i]
        
        