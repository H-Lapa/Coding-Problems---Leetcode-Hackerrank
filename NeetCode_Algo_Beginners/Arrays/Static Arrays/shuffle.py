# https://leetcode.com/problems/shuffle-the-array/

# n = start of second array or middle of array

#Thought bubble

#solution 1
# create an empty array
# for loop through the arra with point i, and n as the second pointer
# assign the new value to the new array
# Time complexity 0(n)


class Solution(object):
    def shuffle(self, nums, n):
        
        
        # j pointer for new array
        j = 0

        #array to store new order of values
        arr = [0] * (2 * n)

        for i in range(n):
            #use n and i as pointers
            arr[j], arr[j+1] = nums[i], nums[n]
            n += 1
            j += 2

        return arr


        