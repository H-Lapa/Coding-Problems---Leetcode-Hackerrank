# https://leetcode.com/problems/fibonacci-number/

#thought bubble
# branches in two directions

#recursion
#stopping statement
# if n =< 1:
#   return n

#recursive statement 
# n minus, forces it to get to the stopping statement
#   self.fib(n-1) + self.fib(n-2)

class Solution(object):
    def fib(self, n):

        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        