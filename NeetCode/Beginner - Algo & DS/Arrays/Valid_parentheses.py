class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            else: 
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if (char == '}' and a != '{') or (char == ')' and a != '(') or (char == ']' and a != '['):
                    return False
        
        if len(stack) != 0:
            return False
        return True

