class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        sortedS1 = sorted(s1)

        for i in range(0, len(s2)):
            
            if sorted(s2[i:i+l]) == sortedS1:
                return True

        return False


# improving  the above solution

# unfinished attempt

from collections import OrderedDict

def createDict(arr):

    result = {}

    for i in arr:

        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        l = len(s1)

        s1Dict = createDict(s1)
        windowDict = createDict(s2[0:l])

        if windowDict == s1Dict:
                return True

        for i in range(0, len(s2)-l+1):

            if windowDict == s1Dict:
                return True

            #remove first value and append a new one

        return False


