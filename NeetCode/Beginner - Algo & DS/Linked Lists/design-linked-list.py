#doubly linked

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        

    def get(self, index):
        #index out of range
        if index >= self.size or index < 0:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.val

        
    def addAtHead(self, val):
        new_node = ListNode(val)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        else:
            self.tail = new_node

        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = ListNode(val)
        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1
        

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:

            new_node = ListNode(val)

            curr = self.head
            for i in range(index-1):
                curr = curr.next

            new_node.next = curr.next
            new_node.prev = curr

            curr.next = new_node
            new_node.next.prev = new_node

        self.size += 1
        
    def deleteAtIndex(self, index):
        if self.head is None or index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next

            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)