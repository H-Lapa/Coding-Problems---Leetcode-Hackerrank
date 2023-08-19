#https://leetcode.com/problems/merge-k-sorted-lists/


#hard question

#thoughts on how to tackle this problem:
class Solution(object):
    def mergeKLists(self, lists):
        #lists is multiple linked lists

        #while loop 
            #see which first value index 0 is the smallest
            #splice away the index 0  of the linkedlist with the smallest value or move the pointer to next
            #continue this until the linked list is empty
            #find a way to deal with being at the end of the linked lists


        return res
        

#first attempt:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = self.merge(res, lists[i])  # Use 'self.' before 'merge'
        
        return res
    
    def merge(self, list1, list2):  # Notice the 'self' parameter
        dummy = ListNode(-1)
        result = dummy  # result will move, but dummy stays at the start

        p1, p2 = list1, list2

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                result.next = p1  # Connect the node
                result = result.next  # Move the pointer
                p1 = p1.next
            else:
                result.next = p2
                result = result.next
                p2 = p2.next

    
        if p1 is not None:
            result.next = p1
        if p2 is not None:
            result.next = p2

        return dummy.next  # Skip the dummy node and return the start of the merged list
