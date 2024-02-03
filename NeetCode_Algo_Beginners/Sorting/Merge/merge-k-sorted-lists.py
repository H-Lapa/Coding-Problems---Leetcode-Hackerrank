# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#thought bubble

# edge cases
#   empty then return None
#   array has only 1 array, return single array

# otherwise while length > 1
# Merge pairs of arrays, until you're left with one
# todo this use a for loop, with an increment of 2


# merge function, between 2 linked lists



class Solution(object):
    def mergeKLists(self, lists):
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:

            mergedLists = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedLists.append(self.merge(l1, l2))

            lists = mergedLists

        return lists[0]


    def merge(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        
        if l2:
            tail.next = l2

        return dummy.next
