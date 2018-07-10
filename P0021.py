# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        point1 = l1
        point2 = l2
        if l1.val <= l2.val:
            head = last = l1
            point1 = l1.next
        else:
            head = last = l2
            point2 = l2.next

        while point1 != None and point2 != None:
            if point1.val <= point2.val:
                last.next = point1
                point1 = point1.next
            else:
                last.next = point2
                point2 = point2.next
            last = last.next
        if point1 != None:
            last.next = point1
        if point2 != None:
            last.next = point2
        return head


s = Solution()
list1 = ListNode(5)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list = s.mergeTwoLists(list1, list2)
while list != None:
    print(list.val)
    list = list.next

