# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1:
            result, lastPoint, nextPoint = self.swapKPairs(head, n - m + 1)
            lastPoint.next = nextPoint
            return result
        else:
            point = head
            for i in range(m - 2):
                point = point.next
            result, lastPoint, nextPoint = self.swapKPairs(point.next, n - m + 1)
            point.next = result
            lastPoint.next = nextPoint
            return head

s = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)
list = s.reverseBetween(list, 1, 5)
while list != None:
    print(list.val)
    list = list.next

