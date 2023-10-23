class Solution(object):
    def isPowerOfFour(self, n):

         if n <= 0:
            return False

        while n >= 1:

            if n == 1:
                return True
                
            if n % 4 == 1:
                break

            n = n / 4

        return False
