# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# understanding recursion in this problem was an issue

class Solution(object):
    def reverseList(self, head):
        
        #thought bubble
        #singly linked list 

        # stopping condition
            # head == None - so empty head scenario potentially
            # head.next == None - stops at the end 
        
        # else

            # reverseList(newHead)

        if not head or not head.next:
            return head
        else:
            #this will force it to get to the end of the list
            newHead = self.reverseList(head.next)

            head.next.next = head
            head.next = None
            return newHead

        