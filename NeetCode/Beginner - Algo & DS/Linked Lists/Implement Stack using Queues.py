from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque([])
        self.queue2 = deque([])

    def push(self, x):
        self.queue.append(x)

        for i in range(len(self.queue2)):
            self.queue.append(self.queue2.popleft())

        self.queue, self.queue2 = self.queue2, self.queue

    def pop(self):
        if len(self.queue2) != 0:
            return self.queue2.popleft()
        

    def top(self):
        if len(self.queue2) != 0:
            return self.queue2[0]
        else:
            return None
        
    def empty(self):
        return len(self.queue2) == 0
     
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.append(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()