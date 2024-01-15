# https://leetcode.com/problems/min-stack/


class MinStack(object):

    def __init__(self):
        self.s = []

    def push(self, val):
        if not self.s:
            self.s.append([val, val])
        else:
            min = self.s[-1][1]
            if val < min:
                min = val
            self.s.append([val, min])
        

    def pop(self):
        self.s.pop()
        
    def top(self):
        return self.s[-1][0]
        
    def getMin(self):
        return self.s[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()