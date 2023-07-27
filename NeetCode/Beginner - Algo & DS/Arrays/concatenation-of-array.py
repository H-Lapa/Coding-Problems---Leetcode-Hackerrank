#mysolution
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)-1
        #create ans of 2 * len(nums)
        ans = [0] * (2 * (n+1))
        print(ans)
        
        #loop through the list for len(nums) & reset when i = len(nums)
        for i in range((2 * (n+1))):
            if i >= n:
                ans[i] = nums[i-n-1]
            else:
                ans[i] = nums[i]

            
        return ans

#optimal solution
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums