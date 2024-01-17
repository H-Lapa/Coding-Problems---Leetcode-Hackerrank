# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #solution idea
        #loop through and add one element from each list, to a new list 
        #if a list becomes empty, you can add the element to the end of the new list

        if not list1:
            return list2

        if not list2:
            return list1

        newList = ListNode()
        curr = newList

        #while the lists are not none
        while list1 and list2:
            if list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        #if any list is empty and the other has a value, it appends the other list to the end 

        # could replace these lines with : curr.next = list1 if list1 else list2
        if not list1 and list2:
            curr.next = list2

        if not list2 and list1:
            curr.next = list1

        #returns new list.next since that is the begining of where we added the new values
        return newList.next