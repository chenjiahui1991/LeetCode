# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        result = head
        prev = head
        point = head.next
        while point is not None:
            if point.val >= prev.val:
                point = point.next
                prev = prev.next
                continue
            if point.val <= result.val:
                prev.next = point.next
                point.next = result
                result = point
                point = prev.next
                continue
            tmp = result
            while tmp.next.val < point.val:
                tmp = tmp.next
            prev.next = point.next
            point.next = tmp.next
            tmp.next = point
            point = prev.next
        return result

head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)

s = Solution()
head = s.insertionSortList(head)
while head is not None:
    print(head.val)
    head = head.next
