# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        result, lastPoint, nextPoint = self.swapKPairs(head, k)
        while nextPoint != None:
            lastPoint.next, tmp, nextPoint = self.swapKPairs(nextPoint, k)
            lastPoint = tmp
        return result

    def swapKPairs(self, head, k):
        if head == None:
            return None
        point = head
        for i in range(k - 1):
            if point.next == None:
                return head, None, None
            point = point.next
        headPoint = point
        nextPoint = point.next
        point1 = head
        point2 = head.next
        head.next = None
        for i in range(k - 1):
            tmp = point2.next
            point2.next = point1
            point1 = point2
            point2 = tmp
        return headPoint, head, nextPoint

s = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)
list = s.reverseKGroup(None, 1)
while list != None:
    print(list.val)
    list = list.next

