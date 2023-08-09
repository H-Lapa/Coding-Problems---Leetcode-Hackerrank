# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        #handling an empty list
        if head is None:
            return None

        prev = None
        curr = head

        while curr is not None:
            #storing the next node after curr for later
            after = curr.next

            #curr pointer is getting set to the node behind it
            curr.next = prev

            #prev and curr are being incremented
            prev = curr
            curr = after
    

        return prev


        


        

        