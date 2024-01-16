# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#thought bubble
#store the values of the first 2 elements
# remove the pointer from the first element 
# then repeat throughout the list
# changing the pointer backwards


class Solution(object):
    def reverseList(self, head):

        #if its empty return what it is
        if not head:
            return None

        #first 2 elements in linked list
        prev = head
        curr = prev.next

        #removing next value of the first element
        prev.next = None

        #reversing the next
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

## recursive solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):

        #checking for empty list or list with only 1 element
        if not head or not head.next:
            return head
        else:
            #recursively calling the function
            newHead = self.reverseList(head.next)
            #reversing the pointer
            head.next.next = head
            #removing the pointer from the first element
            head.next = None

        return newHead
