class Solution(object):
    def isPalindrome(self, s):
        #remove the non-aplhanumeric characters

        phrase = ''.join(filter(str.isalnum, str(s))).lower()
        
        reverse = phrase[::-1]

        print(phrase)
        print(reverse)

        return phrase == reverse