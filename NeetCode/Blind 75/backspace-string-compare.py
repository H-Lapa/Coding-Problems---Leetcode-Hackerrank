class Solution(object):
    def backspaceCompare(self, s, t):

        def buildSentence(x):

            stack = []

            for char in x:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)

            return stack

        return buildSentence(s) == buildSentence(t)
