class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        # i = 0

        # while i < len(s):
        #     if s[i] == '':
        #         s.pop(i)
        #     else:
        #         i += 1

            

        return " ".join(s[::-1])
        