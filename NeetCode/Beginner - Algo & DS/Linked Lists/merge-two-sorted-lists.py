class Solution(object):
    def mergeTwoLists(self, list1, list2):

        newList = ListNode(0)
        curr = newList

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1 is not None:
            curr.next = list1
        if list2 is not None:
            curr.next = list2

        return newList.next


