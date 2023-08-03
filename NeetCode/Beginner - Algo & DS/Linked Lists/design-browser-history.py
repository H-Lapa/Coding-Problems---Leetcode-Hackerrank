#Using Linked Lists, as the goal
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

#optimal solution using arrays

class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url):
        # If we visit a new URL, all the forward history should be cleared
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def back(self, steps):
        # Move back in history by 'steps' or as much as possible
        self.current_index = max(self.current_index - steps, 0)
        return self.history[self.current_index]

    def forward(self, steps):
        # Move forward in history by 'steps' or as much as possible
        self.current_index = min(self.current_index + steps, len(self.history) - 1)
        return self.history[self.current_index]
