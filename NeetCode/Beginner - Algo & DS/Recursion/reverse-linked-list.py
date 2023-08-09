# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # Base case: an empty list or a list with a single node
        if head is None or head.next is None:
            return head
        
        # Recursively reverse the rest of the list
        reversed_tail = self.reverseList(head.next)
        
        # Adjust pointers to reverse the current node's next pointer
        head.next.next = head
        head.next = None
        
        return reversed_tail

        


        

        