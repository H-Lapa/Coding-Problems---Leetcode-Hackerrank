# https://leetcode.com/problems/design-linked-list/

#failed attempt:

class Node():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):

        #if empty return -1 and index in range
        if not self.head or index >= self.length or index < 0:
            return -1

        curr = self.head
        #traverse to find index
        for i in range(index):
            curr = curr.next

        return curr.val
        

    def addAtHead(self, val):
        #if head is empty set the head to the new head
        if not self.head:
            self.head = Node(val, self.tail, None)
            self.tail = self.head
        else:
            #if head exists
            self.head.prev = Node(val, self.head)
            self.head = self.head.prev
        
        self.length += 1


    def addAtTail(self, val):
        if not self.tail:
            self.tail = Node(val, None, None)
            self.head = self.tail
        else:
            self.tail.next = Node(val, None, self.tail)
            self.tail = self.tail.next
        
        self.length += 1
        
        

    def addAtIndex(self, index, val):
        #if empty return -1 and index in range
        if index > self.length or index < 0:
            return
        
        if self.length == 0 and index != 0:
            return

        if index == 0:
            self.addAtHead(val)
            self.length += 1
            return 
            
        if index == self.length:
            self.addAtTail(val)
            self.length += 1
            return 

        curr = self.head
        #traverse to find index
        for i in range(index):
            curr = curr.next

        #now that we are at the index we want the new val to be 
        newNode = Node(val, curr, curr.prev)
        curr.prev.next = newNode
        curr.prev = newNode

        self.length += 1


    def deleteAtIndex(self, index):
        if not self.head or index >= self.length or index < 0 or self.length == 0:
            return 

        #deleting head
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.length -= 1
            return


        #deleting tail
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None  
            self.length -= 1  
            return    

        #deleting index


        curr = self.head

        #traverse to find index
        for i in range(index):
            curr = curr.next

        before = curr.prev
        after = curr.next

        before.next = after
        after.prev = before

        self.length -= 1

        if self.length == 0:
            self.head, self.tail = None, None

        
#Fixed solution:

class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        if not self.head or index >= self.length or index < 0:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        new_node = Node(val, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def addAtTail(self, val):
        new_node = Node(val, None, self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            new_node = Node(val, curr, curr.prev)
            curr.prev.next = new_node
            curr.prev = new_node
            self.length += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if self.length == 1:
                self.tail = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        self.length -= 1

