class ListNode:
    def __init__ (self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        self.curr = ListNode(homepage)

    def visit(self, url):
        #create the new node
        new_node = ListNode(url)

        #set the prev as the current node
        new_node.prev = self.curr
        
        #setting the next node to be the new node
        self.curr.next = new_node

        #update the current node to be the most recent added one
        self.curr = self.curr.next

    def back(self, steps):

        for i in range(steps):
            if self.curr.prev is not None:
                self.curr = self.curr.prev
            else:
                break
                
        return self.curr.val
        
        

    def forward(self, steps):

        for i in range(steps):
            if self.curr.next is not None:
                self.curr = self.curr.next
            else:
                break

        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)