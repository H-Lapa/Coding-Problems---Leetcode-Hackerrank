# https://leetcode.com/problems/baseball-game/

#thought bubble

#solution 1
#loop through each element
#use if statement to commit actions


class Solution(object):
    def calPoints(self, operations):

        newArr = []

        for i in operations:

            if i == "C":
                newArr.pop()
            elif i == "D":
                newArr.append((newArr[len(newArr)-1] * 2))
            elif i == "+":
                newArr.append((newArr[len(newArr)-1] + newArr[len(newArr)-2]))
            else:
                newArr.append(int(i))
        
        return sum(newArr)