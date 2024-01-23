# https://leetcode.com/problems/design-browser-history/

class Node():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory(object):

    def __init__(self, homepage):
        newNode = Node(homepage)
        self.head = newNode
        self.tail = newNode
        self.curr = newNode
        self.pos = 0
        self.length = 1
        

    def visit(self, url):
        # if non-empty
        if self.tail:
            self.curr.next = Node(url, None, self.curr)
            self.curr = self.curr.next
            self.tail = self.curr
            self.pos += 1
            self.length = self.pos + 1
        else:
            newNode = Node(url)
            self.head, self.tail, self.curr = newNode, newNode, newNode
            self.length += 1


    def back(self, steps):
        if not self.curr:
            return None
        if steps >= self.pos:
            self.curr = self.head
        else:
            for i in range(steps):
                self.curr = self.curr.prev
                self.pos -= 1

        return self.curr.val
        

    def forward(self, steps):
        if not self.curr:
            return None
        if steps >= self.length-self.pos-1:
            self.curr = self.tail
        else:
            for i in range(steps):
                self.curr = self.curr.next
                self.pos += 1

        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

#struggled with this one
# new way of completing the challenge, using arrays:

class BrowserHistory(object):

    def __init__(self, homepage):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url):
        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr = len(self.history) - 1

    def back(self, steps):
        if steps >= self.curr:
            self.curr = 0
        else:
            self.curr -= steps

        return self.history[self.curr]
        

    def forward(self, steps):
        if (len(self.history) - 1 - self.curr) < steps:
            self.curr = len(self.history) - 1
        else:
            self.curr += steps

        return self.history[self.curr]
        
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)