# https://leetcode.com/problems/valid-parentheses/


# Thought bubble

#solution 1
# if length is odd return invalid
# use stack, load onto the stack left sided brackets 
# then when come across right sided brackets 
#   we check the top of the stack and pop if they are the same type otherwise we return invalid


class Solution(object):
    def isValid(self, s):

        if (len(s) % 2) == 1:
            print("length issue")
            return False

        stack = []

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif i == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif i == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            elif i == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True 


#solution 1 optmised

#use a dictionary to store the brackets
#then we can use the dictionary to check if the brackets match
#we can also use the dictionary to check if the brackets are left sided or right sided
#so we can load the left sided brackets onto the stack
#then when we come across a right sided bracket we can check if the top of the stack is the same type of bracket
class Solution(object):
    def isValid(self, s):

        if (len(s) % 2) == 1:
            print("length issue")
            return False

        stack = []

        #dictionary of brackets 
        brackets = {')':'(','}':'{',']':'['}

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif stack and stack[-1] == brackets[i]:
                stack.pop()
            else:
                return False

        return not stack




