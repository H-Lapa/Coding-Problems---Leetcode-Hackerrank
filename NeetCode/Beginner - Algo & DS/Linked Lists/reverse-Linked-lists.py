# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        print(head)

        if head == None:
            return head

        prev = None
        curr = head

        while curr != None:

            after = curr.next
            curr.next = prev

            prev = curr
            curr = after
     

    

        print(prev)
        return prev
        
        

