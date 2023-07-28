class MinStack(object):

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, val):

        self.arr.append(val)

        if self.min == [] or val <= self.min[-1]:  
            self.min.append(val)

    def pop(self):

        if self.min[-1] == self.arr[-1]:
            self.min.pop()
        
        self.arr.pop()

    def top(self):

        return self.arr[len(self.arr)-1]

    def getMin(self):

        return self.min[-1]