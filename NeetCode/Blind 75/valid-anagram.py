class Solution(object):
    def isAnagram(self, s, t):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for x in t:
            if x in d:
                d[x] -= 1
            else:
                return False

        print(d)
        return not any(d.values())