#basic solution
class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

#memoization solution
class Solution(object):
    def climbStairs(self, n, memo = {}):
        if n in memo:              
            return memo[n]

        if n <= 2:
            return n
        
        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo) 
        return memo[n]