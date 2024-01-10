# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#Process
# loop through until end
#   if current index is the same at the next index
#       pop the next index

# another potential solution
# loop through array and store values in a dictionary / set
# then create an array with values in dictionary / set
# set nums to be the new array

# Potentially  a two pointer solution

class Solution(object):
    def removeDuplicates(self, nums):
        
        #Solution 1
        i = 0
        while i < len(nums)-1:

            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1



        return len(nums) + 1
        
        