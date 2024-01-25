#thought bubble

# Stopping statement - should stop when reached a 1 step or 2 step scanario
# if n <= 2:
#   return n

# recursive statment
#checks both scenarios of taking both one or two steps at a time 
# self.climbStairs(n-1) + self.climbStairs(n-2)

#need to add memoization - where we add a dictionary to access calculations done before

class Solution(object):
    def climbStairs(self, n, memo={} ):

        #memoization
        #if value has been calculated before, its stored in the dict, and retreived when a value is needed
        if n in memo:
            return memo[n]

        if n <= 2:
            return n 
        else:
            
            #adding to the dictionary
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

            return memo[n]

        