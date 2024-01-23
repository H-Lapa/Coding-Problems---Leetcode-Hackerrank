# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack(object):

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)
        

    def pop(self):
        return self.arr.pop()
        

    def top(self):
        if not self.arr:
            return None
        return self.arr[len(self.arr)-1]
        

    def empty(self):
        return not self.arr
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#using a queue:

from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        temp = self.queue
        self.queue = deque()
        self.queue.append(x)

        for x in temp:
            self.queue.append(x)
        

    def pop(self):
        return self.queue.popleft()
        

    def top(self):
        if not self.queue:
            return None
        return self.queue[0]
        

    def empty(self):
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()